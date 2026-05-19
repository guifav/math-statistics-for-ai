#!/usr/bin/env python3
"""Reconstruct line breaks in markdown cells whose source was serialized as a
single collapsed line.

Background: PRs that re-saved notebooks dropped `\\n` characters in markdown
cells, leaving headings glued to content (`## TitleContent`), list items
concatenated (`1. foo2. bar`), and sentences merged (`text.Other text`).

This script applies conservative heuristics to recover readable structure.
It is safe to re-run: cells that already contain real line structure are
left untouched.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


HEADING_MARKER_RE = re.compile(r"#{1,6} ")
PUNCT_CAPITAL_RE = re.compile(r"([?!:])([A-Z])")
# Match any word ending in 3+ lowercase letters glued to an uppercase letter.
# CamelCase compounds (`EfficientNet`, `LangChain`, `cProfile`) are filtered
# downstream by inspecting the surrounding word's casing.
LOWER_UPPER_RE = re.compile(r"([a-z]{3,})([A-Z])")
# Lookbehind is "non-digit then lowercase letter or closing paren" — splits
# list items glued to a real word (`treino2. Item`) or to a parenthetical
# (`)8. Item`), but never inside dimensions (`7x7. Isso`), compound numbers
# (`13. ...`), or single-letter variable names (`L2. ...`).
NUMBERED_ITEM_INLINE_RE = re.compile(r"(?<=[^0-9][a-z\)])(?=\d{1,2}\. [A-Za-z*\-])")
# Require a lowercase letter immediately before so we don't mistake math like
# `F(5) - F(2)` for a bullet list. List items glued to prose always follow a
# word ending in a lowercase letter (`grafo- **PageRank**`, `treino- Camada`).
BULLET_ITEM_INLINE_RE = re.compile(r"(?<=[a-z])(?=- [A-Za-z*])")
PUNCT_BEFORE_LIST_RE = re.compile(r"([?!:])\s*(?=\d{1,2}\. )")
COLON_BEFORE_BULLET_RE = re.compile(r"([?!:])(?=- [A-Za-z*])")
SENTENCE_BOUNDARY_RE = re.compile(r"(?<=[a-z\)\]])\.(?=[A-Z][a-z])")
PAREN_NEW_SENTENCE_RE = re.compile(r"(\))([A-Z][a-z])")
# Only fire when the bold marker is glued directly to a lowercase letter
# (i.e. the corruption pattern `text**Bold**`). Don't fire after `1. `, `- `,
# `. `, or any whitespace — those are valid list/paragraph layouts already.
BOLD_PARAGRAPH_RE = re.compile(r"(?<=[a-z])(?=\*\*[A-Z])")
LOWER_UPPER_INLINE_RE = re.compile(r"([a-z]{3,})([A-Z])")


def needs_restoration(text: str) -> bool:
    """Return True when the cell shows fingerprints of newline-stripping corruption.

    Looks for:
    - heading marker mid-string,
    - inline numbered/bullet list glued to prose,
    - sentence boundary with no space (`word.Capital`),
    - lower-Upper transition with a real word ending (`treinadosObjetivo`).
    Exits early if the cell is already well-structured (5+ newlines) or looks
    like a Python code cell that was mistyped as markdown.
    """
    if not text or len(text) < 40:
        return False
    if _looks_like_python_code(text):
        return False
    for match in HEADING_MARKER_RE.finditer(text):
        if match.start() > 0 and text[match.start() - 1] != "\n":
            return True
    # Check for corruption signatures anywhere in the cell, not just in
    # collapsed blobs — a partially-restored cell can still have a glued
    # heading on a single line.
    for line in text.split("\n"):
        if line.startswith("#") and re.search(r"[a-z]{3,}[A-Z]", line):
            return True
    if NUMBERED_ITEM_INLINE_RE.search(text):
        return True
    if BULLET_ITEM_INLINE_RE.search(text):
        return True
    if re.search(r"[a-z]\.[A-Z][a-z]", text):
        return True
    if re.search(r"[a-z]{3,}[A-Z]", text):
        return True
    return False


def _looks_like_python_code(text: str) -> bool:
    """Heuristic: markdown cell that is actually Python code (a tooling bug).

    Such cells should be hand-fixed (converted to code or wrapped in a fence),
    never auto-restored.
    """
    has_python_call = bool(re.search(r"\bprint\s*\(", text))
    has_import = bool(re.search(r"^\s*(import |from \S+ import)", text, re.M))
    has_def_class = bool(re.search(r"^\s*(def |class )\w+", text, re.M))
    if has_python_call and (has_import or has_def_class):
        return True
    # Block of comment-only lines plus a print/assignment.
    comment_lines = [
        ln for ln in text.split("\n") if ln.strip().startswith("# ")
    ]
    if len(comment_lines) >= 2 and has_python_call:
        return True
    return False


def split_at_heading_markers(text: str) -> list[str]:
    """Slice text so every `#{1,6} ` starts a new block."""
    blocks: list[str] = []
    cursor = 0
    for match in HEADING_MARKER_RE.finditer(text):
        start = match.start()
        if start > cursor:
            chunk = text[cursor:start].strip()
            if chunk:
                blocks.append(chunk)
        cursor = start
    tail = text[cursor:].strip()
    if tail:
        blocks.append(tail)
    return blocks


def split_heading_from_content(block: str) -> list[str]:
    """If a heading line has content glued after the title, split them.

    Operates on the FIRST line of the block (the heading line). Any
    subsequent lines stay attached to the content portion.

    Considers four candidate boundaries (punct+capital, punct+list, glued
    bullet, lower-Upper word junction) and chooses the *earliest* one — the
    real heading text is the shortest fragment.
    """
    first_line, _, remainder = block.partition("\n")
    m = re.match(r"^(#{1,6}\s+)(.+)$", first_line)
    if not m:
        return [block]
    prefix, rest = m.group(1), m.group(2)

    candidates: list[int] = []

    punct = PUNCT_CAPITAL_RE.search(rest)
    if punct and punct.end(1) >= 5:
        candidates.append(punct.end(1))

    punct_list = re.search(r"([?!:])\s*(\d+\. )", rest)
    if punct_list:
        candidates.append(punct_list.end(1))

    bullet = re.search(r"([a-zA-Z])\s*(?=- [A-Za-z*])", rest)
    if bullet and bullet.end(1) >= 4:
        candidates.append(bullet.end(1))

    lower_upper = LOWER_UPPER_RE.search(rest)
    if lower_upper and lower_upper.end(1) >= 5:
        candidates.append(lower_upper.end(1))

    if not candidates:
        return [block]

    split_at = min(candidates)
    head = f"{prefix}{rest[:split_at]}"
    tail_head = rest[split_at:].strip()
    pieces = [head]
    if tail_head:
        pieces.append(tail_head)
    if remainder.strip():
        pieces.append(remainder.strip())
    return pieces


def _split_lower_upper(text: str) -> str:
    """Split `wordWord` joinings unless they look like a real CamelCase compound.

    Real CamelCase tokens (`EfficientNet`, `GridSearchCV`, `LangChain`) keep
    their lowercase runs short (<=8) and the surrounding word starts with an
    uppercase letter. Corruption joinings — heading-into-content or
    sentence-into-sentence — typically yield a lowercase-starting "word" or a
    very long lowercase run.
    """

    def replacer(match: re.Match[str]) -> str:
        lower_chunk = match.group(1)
        # Walk back to find the start of the surrounding word.
        word_start = match.start()
        while word_start > 0 and text[word_start - 1].isalpha():
            word_start -= 1
        starts_upper = (
            word_start < len(text) and text[word_start].isupper()
        )
        if starts_upper and len(lower_chunk) <= 8:
            return match.group(0)
        return f"{lower_chunk}\n{match.group(2)}"

    return LOWER_UPPER_INLINE_RE.sub(replacer, text)


def split_inline_structure(block: str) -> str:
    """Restore newlines between concatenated paragraphs, list items, bold runs."""
    block = PUNCT_BEFORE_LIST_RE.sub(r"\1\n\n", block)
    block = COLON_BEFORE_BULLET_RE.sub(r"\1\n\n", block)
    block = NUMBERED_ITEM_INLINE_RE.sub("\n", block)
    block = BULLET_ITEM_INLINE_RE.sub("\n", block)
    block = SENTENCE_BOUNDARY_RE.sub(".\n\n", block)
    block = PAREN_NEW_SENTENCE_RE.sub(r"\1\n\n\2", block)
    block = BOLD_PARAGRAPH_RE.sub("\n\n", block)
    block = _split_lower_upper(block)
    return block


def _restore_prose(text: str) -> str:
    raw_blocks = split_at_heading_markers(text)
    expanded: list[str] = []
    for block in raw_blocks:
        if block.startswith("#"):
            expanded.extend(split_heading_from_content(block))
        else:
            expanded.append(block)
    expanded = [split_inline_structure(b) for b in expanded]

    # Join pieces with paragraph breaks, then enforce heading spacing without
    # discarding existing `\n\n` paragraph separators inside each piece.
    combined = "\n\n".join(piece.strip() for piece in expanded if piece.strip())
    combined = re.sub(
        r"(?<!^)(?<!\n\n)(?<!#)(#{1,6} )", r"\n\n\1", combined
    )
    combined = re.sub(
        r"^(#{1,6} [^\n]+)\n(?!\n|$)", r"\1\n\n", combined, flags=re.M
    )
    combined = re.sub(r"\n{3,}", "\n\n", combined)
    return combined.strip()


FENCE_RE = re.compile(r"```([^\n`]*?)```|```([^\n`]*)\n([\s\S]*?)```")
FENCE_TOKEN_KNOWN_LANGS = {
    "python", "py", "bash", "sh", "shell", "sql", "json", "yaml", "toml",
    "javascript", "js", "typescript", "ts", "html", "css", "markdown", "md",
    "rust", "go", "java", "cpp", "c", "ruby", "rb", "r", "php", "swift",
    "kotlin", "scala", "perl", "lua",
}
TREE_BRANCH_CHARS = "├└│"


def _restore_fence_content(lang: str, content: str) -> str:
    """Re-insert line breaks inside a collapsed fenced code/diagram block.

    Safe to call on partially-restored content: each regex only inserts a
    newline at a corruption boundary, so a fence that's already clean is a
    no-op.
    """
    if len(content) < 40:
        return content

    if lang.lower() in {"python", "py"}:
        # Insert newline before every `#` that is glued to alphanumeric (or
        # a closing quote/paren) — splits "code# next-comment" patterns.
        content = re.sub(r'(?<=[a-zA-Z0-9_\)\]\}"\'])(?=#\s)', "\n", content)
        # `)identifier_=` -> `)\nidentifier_=` (statement boundary).
        content = re.sub(r"(?<=\))(?=[a-zA-Z_][a-zA-Z0-9_]*\s*=)", "\n", content)
        # `)keyword` -> `)\nkeyword` (statement boundary before for/while/if).
        content = re.sub(
            r"(?<=\))(?=(?:for|while|if|elif|else|return|yield|with|try|except|finally|raise|class|def|import|from|pass|break|continue)\s)",
            "\n",
            content,
        )
        # Close paren/bracket followed by capital-prefixed identifier
        # (e.g. `y.std()X_train`, `data[0]Y_test`).
        content = re.sub(
            r"([\)\]])(?=[A-Z][a-zA-Z_0-9]*\s*[,=\.\(])",
            r"\1\n",
            content,
        )
        # NOTE: word glued to a single-letter+underscore identifier (e.g.
        # `testey_normalized = ...`) used to be auto-fixed by a regex, but
        # the same regex also fired on legit identifiers like `mean_train` at
        # line start (greedy backtracking would pick `mea` + `n_train`). The
        # autocorrect was removed; the validator instead reports these and
        # they are repaired by hand.
        # `importaresultado = ...` (lowercase comment word glued to lowercase
        # variable assignment with no identifier-boundary character between
        # them) is also not auto-fixed — the regex cannot pick the right
        # split point without a dictionary. Both cases are reported by the
        # validator's rule 10 for manual repair.
        # All-caps comment word followed by lowercase code.
        content = re.sub(r"(#[^\n]*[A-Z]{3,})(?=[a-z])", r"\1\n", content)
        # `wordA *` or `wordA = ` — statement starts with a single uppercase
        # operand glued to a comment word. Operator/space/newline must follow.
        content = re.sub(
            r"(?<=[a-z]{3})(?=[A-Z](?:\s*[\*+\-/=<>%&|@]| =|$))",
            "\n",
            content,
        )
        # Lowercase letter followed by uppercase letter + lowercase glued
        # (e.g. `matricialA @ B`). Skip when the surrounding word is a
        # legitimate CamelCase token such as `ValueError`, `DataFrame`,
        # `KFold` — those start with an uppercase letter.
        content = _split_lower_upper(content)
    elif any(ch in content for ch in TREE_BRANCH_CHARS):
        # Tree diagrams: split before any branch marker.
        content = re.sub(r"(?<=.)(?=[│├└])", "\n", content)
        content = re.sub(r"\n{2,}", "\n", content)

    return content


def _restore_fence(match: re.Match[str]) -> str:
    no_break_group = match.group(1)
    if no_break_group is not None:
        # ```lang+content``` all on one line; split lang from content if a known
        # language is glued to code, otherwise treat the whole thing as content.
        body = no_break_group
        for lang in sorted(FENCE_TOKEN_KNOWN_LANGS, key=len, reverse=True):
            if body.startswith(lang) and len(body) > len(lang) and body[len(lang)] not in (" ", "\n"):
                rest = body[len(lang):]
                rest = _restore_fence_content(lang, rest).strip("\n")
                return f"```{lang}\n{rest}\n```"
        # No known lang prefix; still try restoring as best-effort
        restored = _restore_fence_content("", body).strip("\n")
        if "\n" in restored:
            return f"```\n{restored}\n```"
        return match.group(0)
    # Form ```lang\ncontent\n``` (already has at least one newline after lang).
    lang = match.group(2)
    content = match.group(3)
    restored = _restore_fence_content(lang, content).strip("\n")
    return f"```{lang}\n{restored}\n```"


def restore_text(text: str) -> str:
    if not needs_restoration(text) and not FENCE_RE.search(text):
        return text

    pieces: list[str] = []
    cursor = 0
    for fence in FENCE_RE.finditer(text):
        if fence.start() > cursor:
            pieces.append(_restore_prose(text[cursor:fence.start()]))
        pieces.append(_restore_fence(fence))
        cursor = fence.end()
    if cursor < len(text):
        pieces.append(_restore_prose(text[cursor:]))

    return "\n\n".join(p for p in pieces if p).strip()


def restore_notebook(path: Path, dry_run: bool = False) -> tuple[int, int]:
    nb = json.loads(path.read_text(encoding="utf-8"))
    changed = 0
    total_md = 0
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "markdown":
            continue
        total_md += 1
        src = cell.get("source", "")
        text = "".join(src) if isinstance(src, list) else str(src)
        restored = restore_text(text)
        if restored == text:
            continue
        changed += 1
        lines = restored.split("\n")
        new_source: list[str] = []
        for i, line in enumerate(lines):
            if i < len(lines) - 1:
                new_source.append(line + "\n")
            elif line:
                new_source.append(line)
        cell["source"] = new_source
    if changed and not dry_run:
        path.write_text(
            json.dumps(nb, ensure_ascii=False, indent=1) + "\n",
            encoding="utf-8",
        )
    return changed, total_md


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", help="Notebook files to restore")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    for raw in args.paths:
        path = Path(raw)
        if not path.exists():
            print(f"skip (not found): {path}", file=sys.stderr)
            continue
        changed, total = restore_notebook(path, dry_run=args.dry_run)
        flag = "(dry-run) " if args.dry_run else ""
        print(f"{flag}{path}: restored {changed}/{total} markdown cells")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
