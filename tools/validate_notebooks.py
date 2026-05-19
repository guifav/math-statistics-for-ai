#!/usr/bin/env python3
"""Lightweight repository validation for notebook quality gates."""

from __future__ import annotations

import ast
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK_ROOT = ROOT / "notebooks"
HEADER_MARKER = "<!-- notebook-header -->"
LEGACY_PLACEHOLDER = "TO" "DO"
TEMP_SESSION_PATH = "/sessions" "/"
LEGACY_WORKDIR = "notebooks-math" "&statistics"
NOTEBOOK_REF_RE = re.compile(r"(?<![\w./-])([A-Za-z0-9_][A-Za-z0-9_\-]*\.ipynb)")

# Generic placeholder phrases that indicate unfilled scaffolding. Matched case-
# insensitive. Heuristic only flags these when they appear in code cells or when
# they dominate a short markdown cell, to avoid false positives in didactic text
# that legitimately mentions things like "o seu codigo pode ser otimizado".
GENERIC_PLACEHOLDER_RE = re.compile(
    r"\b(seu\s+c[oó]digo(\s+aqui)?"
    r"|sua\s+resposta(\s+aqui)?"
    r"|complete\s+aqui"
    r"|escreva\s+sua"
    r"|substitua\s+pelo)\b",
    re.IGNORECASE,
)

# Keywords that, when present inside a "comment-only" code cell, strongly
# suggest real code was accidentally collapsed into a comment block.
CODE_KEYWORDS_IN_COMMENT_RE = re.compile(
    r"\b(def|import|from|return|class|for|while|if|elif|else|print|lambda|with|try|except)\b\s*[\(:]?"
)

# nbformat 4.5+ requires every cell to carry an id matching ^[a-zA-Z0-9_-]+$.
CELL_ID_RE = re.compile(r"^[a-zA-Z0-9_-]+$")

# Markdown cells whose source looks like Python code (multiple top-level
# Python statements + a print/import) usually indicate a cell that was meant
# to be a code cell. They escape the existing code-only-comment heuristic
# because that heuristic only runs on code cells.
MD_CODE_KEYWORDS = re.compile(
    r"^\s*(print\s*\(|def \w+\s*\(|class \w+\s*[\(:]|import \S+|from \S+ import)",
    re.M,
)

# Heading marker glued to non-heading content on the same line (the
# newline-stripping corruption fingerprint).
COLLAPSED_HEADING_RE = re.compile(r"^#{1,6} [^\n]{6,}[a-z]{3,}[A-Z]", re.M)

# Triple-backtick fence (any language) — used to strip code blocks before
# running prose-only validators that would false-fire on `# python comment`.
FENCE_BLOCK_RE = re.compile(r"```[\s\S]*?```")

# Match a fenced block and inspect its first line for newline-stripping
# fingerprints (multiple `#` comments glued together or language tag glued to
# code on the same line as the opener). Multi-line blocks are extracted and
# only the OPENING line is examined, so legit multi-line code is safe.
FENCE_OPEN_RE = re.compile(r"```([^\n]*)")
KNOWN_FENCE_LANGS = (
    "python", "py", "bash", "sh", "shell", "sql", "json", "yaml", "toml",
    "javascript", "js", "typescript", "ts", "html", "css", "markdown", "md",
    "rust", "go", "java", "cpp", "c", "ruby", "rb", "r", "php", "swift",
    "kotlin", "scala", "perl", "lua",
)
GLUED_COMMENT_RE = re.compile(r"[a-zA-Z0-9\)\]\}]#\s*[A-Za-z]")

# Full-fence-body extraction used to inspect inner lines for residual
# corruption (the opening-line check alone misses content inside the fence).
FENCE_BODY_RE = re.compile(r"```([^\n]*)\n([\s\S]*?)```", re.MULTILINE)

# Closing paren/bracket glued to an uppercase identifier (e.g. `y.std()X_train`).
CLOSER_GLUED_UPPER_RE = re.compile(r"[\)\]][A-Z][a-zA-Z_0-9]*\s*[,=\.\(]")

# Lowercase word ending glued to an underscore-style identifier whose tuple
# eventually leads to an `=` assignment (`testey_normalized = `,
# `barX_train, X_test = split(...)`). Restricted to `=` (not bare call) so
# legit code embedded in comments like `# torch.manual_seed(42)` isn't
# flagged.
WORD_GLUED_UNDERSCORE_ID_RE = re.compile(
    r"(?<![a-zA-Z0-9_\.])[a-z]{3,}[a-zA-Z]_[a-zA-Z]\w*(?:\s*,\s*\w+)*\s*="
)

# Lowercase word glued to lowercase identifier with assignment — ambiguous
# boundary that the restorer cannot fix automatically. Flagged for human
# review (e.g. `importaresultado = B @ A`, `wordvariable = ...`).
WORD_GLUED_LOWER_ASSIGN_RE = re.compile(
    r"(?<![a-zA-Z0-9_])[a-z]{4,}[a-z][a-z_0-9]{6,}\s*=\s*[A-Za-z\d\(\[\{]"
)

# CamelCase boundary that suggests a comment-end glued to code
# (`matricialA @ B`, `decisaoIf ...`). We require a non-Camel context to
# avoid flagging legitimate compound names like `KFoldClassifier`.
LOWER_UPPER_OPERATOR_RE = re.compile(
    r"(?<![A-Z])[a-z]{4,}[A-Z](?:\s*[\*+\-/=<>%&|@,])"
)

# Comment word glued directly to a Python keyword (`sempreif `, `endwhile `).
# Restricted to a known keyword followed by an opening paren/space to avoid
# matching arbitrary identifiers.
WORD_GLUED_KEYWORD_RE = re.compile(
    r"(?<![A-Za-z0-9_])[a-z]{3,}"
    r"(?:if|while|for|return|raise|elif|else|pass|break|continue|yield|with|try|except|finally|class|def|import|from)"
    r"[ \(]"
)

# Bullet item glued to the previous line OUTSIDE a fence (e.g.
# `BPTT)- **5A_1**` or `dados?- [ ] checkbox`). The `(?<![\s])` keeps math
# `F(5) - F(2)` safe.
BULLET_GLUED_RE = re.compile(
    r"(?<![\s\-])(?<=[A-Za-z\?\.!\)])- (?:\[|[A-Za-z*])"
)


def _first_line_has_glued_lang(first_line: str) -> bool:
    """Detect `lang` glued to identifier on a fence opener.

    Returns True only when the line starts with a known language name and
    is *immediately* followed by another letter/underscore — i.e. the lang
    tag was concatenated to code by the newline-stripping corruption.

    Languages are tested longest-first so that `python` is matched before
    `py` and we never report a false positive on a clean `python` opener.
    """
    for lang in sorted(KNOWN_FENCE_LANGS, key=len, reverse=True):
        if first_line.startswith(lang):
            rest = first_line[len(lang):]
            if not rest:
                return False
            return rest[0].isalpha() or rest[0] == "_"
    return False


def _non_empty_lines(text: str) -> list[str]:
    return [line for line in text.splitlines() if line.strip()]


def _is_comment_only_code(text: str) -> bool:
    """Heuristic: detect code cells that are entirely commented out.

    Returns True only when at least 3 non-empty lines exist AND every non-empty
    line starts with '#'. Short comment-only cells (1-2 lines) are allowed as
    they often serve as legitimate section markers. We also require that the
    comment block looks like real code (long line or contains code keywords),
    otherwise prose-only `# Configuracao de parametros` cells would be flagged.
    """
    lines = _non_empty_lines(text)
    if len(lines) < 3:
        return False
    if not all(line.lstrip().startswith("#") for line in lines):
        return False
    # Require evidence that real code is hidden inside the comments.
    if any(len(line) >= 80 for line in lines):
        return True
    joined = "\n".join(lines)
    return bool(CODE_KEYWORDS_IN_COMMENT_RE.search(joined))


def _is_stub_solution(cell: dict, text: str) -> bool:
    """Heuristic: detect solution-tagged code cells that are empty/stubs."""
    tags = (cell.get("metadata") or {}).get("tags") or []
    if "solution" not in tags:
        return False
    lines = _non_empty_lines(text)
    if not lines or len(lines) > 3:
        return False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("#"):
            continue
        if stripped in {"pass", "return", "..."}:
            continue
        if re.fullmatch(r"return\s+.*", stripped) and "..." in stripped:
            continue
        if re.fullmatch(r"print\s*\(.*\)", stripped):
            continue
        if "resolvida" in stripped.lower() and "..." in stripped:
            continue
        return False
    return True


def _has_generic_placeholder(cell_type: str, text: str) -> bool:
    """Heuristic for rule 4. Only flags clear scaffolding placeholders.

    - In code cells: any match counts (these almost never appear in real code).
    - In markdown cells: only flag when the placeholder dominates a short cell
      (<= 2 non-empty lines), to avoid false positives in didactic prose.
    """
    match = GENERIC_PLACEHOLDER_RE.search(text)
    if not match:
        return False
    if cell_type == "code":
        return True
    lines = _non_empty_lines(text)
    return len(lines) <= 2


def iter_notebooks() -> list[Path]:
    return sorted(NOTEBOOK_ROOT.rglob("*.ipynb"))


def source_text(cell: dict) -> str:
    source = cell.get("source", "")
    if isinstance(source, list):
        return "".join(source)
    return str(source)


def should_parse_python(source: str) -> bool:
    stripped = source.lstrip()
    return not stripped.startswith(("%", "!", "%%"))


def _check_exercise_solution_completeness(path: Path, cells: list) -> list[str]:
    """Rule 5: every contiguous 'exercise' group must be followed by a 'solution' cell.

    A group is a run of consecutive cells with tag 'exercise'. We look for a
    'solution'-tagged cell either within the group or in the next 3 cells.
    Missing solutions are reported with the group's cell range for easy triage.
    """
    errors: list[str] = []
    n = len(cells)
    i = 0
    while i < n:
        tags = (cells[i].get("metadata") or {}).get("tags") or []
        if "exercise" not in tags:
            i += 1
            continue
        start = i
        while i < n and "exercise" in ((cells[i].get("metadata") or {}).get("tags") or []):
            i += 1
        end_exclusive = i
        has_solution = False
        for k in range(start, min(end_exclusive + 3, n)):
            k_tags = (cells[k].get("metadata") or {}).get("tags") or []
            if "solution" in k_tags:
                has_solution = True
                break
        if not has_solution:
            rng = f"{start + 1}" if end_exclusive - start == 1 else f"{start + 1}..{end_exclusive}"
            errors.append(
                f"{path}: exercise group at cell {rng} has no adjacent 'solution' cell "
                f"(must appear inside the group or within 3 cells after it)"
            )
    return errors


def _md_looks_like_python(text: str) -> bool:
    """Heuristic for rule 6: markdown cell containing raw Python code.

    Triggers when the cell has 2+ Python-style top-level statements AND no
    triple-backtick fence framing them. Such cells should be code cells (or
    wrapped in a fence) — leaving them as markdown breaks rendering and hides
    the code from execution.
    """
    if "```" in text:
        return False
    hits = MD_CODE_KEYWORDS.findall(text)
    return len(hits) >= 2


def validate_notebook(path: Path, notebook_names: set[str]) -> list[str]:
    errors: list[str] = []

    try:
        nb = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # pragma: no cover - error string is the behavior
        return [f"{path}: invalid JSON: {exc}"]

    cells = nb.get("cells", [])
    if not cells:
        errors.append(f"{path}: notebook has no cells")
        return errors

    metadata = nb.get("metadata", {})
    if not metadata.get("kernelspec"):
        errors.append(f"{path}: missing kernelspec metadata")

    first_cell = cells[0]
    first_text = source_text(first_cell)
    if first_cell.get("cell_type") != "markdown" or HEADER_MARKER not in first_text:
        errors.append(f"{path}: first cell must be the standardized notebook header")

    if not metadata.get("course_title") or not metadata.get("course_description"):
        errors.append(f"{path}: missing course title/description metadata")

    nbformat_minor = nb.get("nbformat_minor", 0)
    requires_cell_ids = nb.get("nbformat", 4) >= 4 and nbformat_minor >= 5

    previous_markdown_norm: str | None = None
    for cell_index, cell in enumerate(cells, start=1):
        text = source_text(cell)
        cell_type = cell.get("cell_type")

        if LEGACY_PLACEHOLDER in text:
            errors.append(
                f"{path}: cell {cell_index}: use 'TAREFA DO ALUNO' instead of the legacy placeholder"
            )
        if TEMP_SESSION_PATH in text or LEGACY_WORKDIR in text:
            errors.append(f"{path}: cell {cell_index}: contains temporary generation path")
        for match in NOTEBOOK_REF_RE.finditer(text):
            notebook_name = match.group(1)
            if notebook_name not in notebook_names:
                errors.append(
                    f"{path}: cell {cell_index}: references missing notebook {notebook_name}"
                )

        # Rule 6: every cell must carry a valid id in nbformat 4.5+.
        if requires_cell_ids:
            cell_id = cell.get("id")
            if cell_id is None or not cell_id or not CELL_ID_RE.match(cell_id):
                errors.append(
                    f"{path}: cell {cell_index}: invalid cell id {cell_id!r} "
                    f"(must match ^[a-zA-Z0-9_-]+$)"
                )

        # Rule 1: consecutive duplicate markdown cells.
        if cell_type == "markdown":
            normalized = text.strip()
            if normalized and previous_markdown_norm == normalized:
                errors.append(
                    f"{path}: cell {cell_index}: consecutive duplicate markdown cell"
                )
            previous_markdown_norm = normalized

            # Rule 7: markdown cell that is actually Python code (should be a
            # code cell, or wrapped in a triple-backtick fence).
            if _md_looks_like_python(text):
                errors.append(
                    f"{path}: cell {cell_index}: markdown cell contains raw Python "
                    f"code without a fence (should be a code cell)"
                )

            # Strip fence blocks before checking heading/code rules — Python
            # comments inside a ` ```python `` block start with `# ` and would
            # otherwise be misread as markdown headings.
            text_no_fences = FENCE_BLOCK_RE.sub("", text)

            # Rule 8: heading marker glued to non-heading content on the
            # same line — fingerprint of the newline-stripping corruption.
            if COLLAPSED_HEADING_RE.search(text_no_fences):
                errors.append(
                    f"{path}: cell {cell_index}: heading is glued to content on "
                    f"the same line (markdown line breaks were stripped)"
                )

            # Rule 9: fenced code block opener glued to code on same line, or
            # any fence whose inner body has comments concatenated without
            # newlines (`text# next-comment`). Multi-line fences with clean
            # comment-per-line layout are not flagged.
            for fm in FENCE_OPEN_RE.finditer(text):
                first_line = fm.group(1)
                if _first_line_has_glued_lang(first_line):
                    errors.append(
                        f"{path}: cell {cell_index}: fenced code block opener "
                        f"is glued to code on the same line "
                        f"(```{first_line[:30]}...)"
                    )
                    break
                if GLUED_COMMENT_RE.search(first_line):
                    errors.append(
                        f"{path}: cell {cell_index}: fenced code block has "
                        f"multiple `#` comments glued without newlines"
                    )
                    break

            # Rule 10: fence INNER body has residual corruption fingerprints.
            # Scans the body line by line. Inner identifiers with underscores
            # are common in legit Python (`read_csv`, `query_vec`), so the
            # word-glued-to-underscore-identifier check is only applied to
            # lines that START with `#` (Python comments) — where the
            # corruption shows up as a comment glued to a code statement.
            for fbm in FENCE_BODY_RE.finditer(text):
                body = fbm.group(2)
                for body_line in body.split("\n"):
                    if GLUED_COMMENT_RE.search(body_line):
                        errors.append(
                            f"{path}: cell {cell_index}: fenced code block "
                            f"has comments glued without a newline "
                            f"(`{body_line[:60]}`)"
                        )
                        break
                    if CLOSER_GLUED_UPPER_RE.search(body_line):
                        errors.append(
                            f"{path}: cell {cell_index}: fenced code block "
                            f"has `)X_identifier` glued statement boundary "
                            f"(`{body_line[:60]}`)"
                        )
                        break
                    is_comment_line = body_line.lstrip().startswith("#")
                    if is_comment_line and WORD_GLUED_UNDERSCORE_ID_RE.search(body_line):
                        errors.append(
                            f"{path}: cell {cell_index}: fenced code block "
                            f"has comment word glued to underscore identifier "
                            f"(`{body_line[:60]}`)"
                        )
                        break
                    if is_comment_line and WORD_GLUED_LOWER_ASSIGN_RE.search(body_line):
                        errors.append(
                            f"{path}: cell {cell_index}: fenced code block "
                            f"has ambiguous word-glued-to-variable boundary "
                            f"that needs manual fix (`{body_line[:60]}`)"
                        )
                        break
                    if is_comment_line and LOWER_UPPER_OPERATOR_RE.search(body_line):
                        errors.append(
                            f"{path}: cell {cell_index}: fenced code block "
                            f"has lowercase-Upper boundary glued to operator "
                            f"(`{body_line[:60]}`)"
                        )
                        break
                    if WORD_GLUED_KEYWORD_RE.search(body_line):
                        errors.append(
                            f"{path}: cell {cell_index}: fenced code block "
                            f"has word glued to Python keyword "
                            f"(`{body_line[:60]}`)"
                        )
                        break
                else:
                    continue
                break

            # Rule 11: bullet item glued to prior content OUTSIDE a fence
            # (`BPTT)- **5A_1**`, `dados?- [ ] checkbox`). Math like
            # `F(5) - F(2)` (with whitespace around the dash) is not flagged.
            text_no_fences = FENCE_BLOCK_RE.sub("", text)
            if BULLET_GLUED_RE.search(text_no_fences):
                match = BULLET_GLUED_RE.search(text_no_fences)
                start = max(0, match.start() - 30)
                end = min(len(text_no_fences), match.end() + 30)
                errors.append(
                    f"{path}: cell {cell_index}: bullet item glued to prior "
                    f"content (`{text_no_fences[start:end]!r}`)"
                )
        else:
            previous_markdown_norm = None

        # Rule 4: generic scaffolding placeholders.
        # Exercise-tagged cells are deliberately scaffolded for students
        # (e.g. `None  # sua resposta aqui`), so we skip them to avoid noise.
        cell_tags = (cell.get("metadata") or {}).get("tags") or []
        if "exercise" not in cell_tags and _has_generic_placeholder(cell_type or "", text):
            errors.append(
                f"{path}: cell {cell_index}: contains generic placeholder text"
            )

        if cell_type != "code":
            continue

        # Rule 6: outputs are allowed (didactic render), but with two guards:
        # (a) never commit an error output — that means a cell was committed
        #     in a broken state;
        # (b) never commit any output for an `exercise`-only scaffold — those
        #     cells are stubs for the student to fill in.
        outputs = cell.get("outputs") or []
        for output in outputs:
            if (output or {}).get("output_type") == "error":
                ename = (output or {}).get("ename", "error")
                errors.append(
                    f"{path}: cell {cell_index}: committed output contains error ({ename})"
                )
                break
        if outputs and "exercise" in cell_tags and "solution" not in cell_tags:
            errors.append(
                f"{path}: cell {cell_index}: exercise-only scaffold must not carry outputs"
            )

        # Rule 2: code cell that is entirely a comment block (likely broken).
        if _is_comment_only_code(text):
            errors.append(
                f"{path}: cell {cell_index}: code cell appears to contain only comments "
                f"(possible broken code)"
            )

        # Rule 3: solution cell that is a stub.
        if _is_stub_solution(cell, text):
            errors.append(
                f"{path}: cell {cell_index}: solution cell appears to be empty/stub"
            )

        if not should_parse_python(text):
            continue
        try:
            ast.parse(text)
        except SyntaxError as exc:
            errors.append(
                f"{path}: cell {cell_index}: Python syntax error at line "
                f"{exc.lineno}: {exc.msg}"
            )

    # Rule 5: exercise-solution completeness.
    errors.extend(_check_exercise_solution_completeness(path, cells))

    return errors


def validate_repository() -> list[str]:
    errors: list[str] = []
    notebooks = iter_notebooks()
    if not notebooks:
        errors.append("notebooks/: no .ipynb files found")
    notebook_names = {path.name for path in notebooks}

    root_notebooks = sorted(ROOT.glob("*.ipynb"))
    if root_notebooks:
        names = ", ".join(path.name for path in root_notebooks)
        errors.append(f"repository root contains notebooks; move them under notebooks/: {names}")

    for path in notebooks:
        errors.extend(validate_notebook(path, notebook_names))

    allowed_root_entries = {
        "README.md",
        "LICENSE",
        "CONTRIBUTING.md",
        "CODE_OF_CONDUCT.md",
        "SECURITY.md",
        "requirements.txt",
        "requirements-gpu.txt",
        ".gitignore",
        ".github",
        "tools",
        "notebooks",
        ".git",
    }

    for path in sorted(ROOT.glob("*")):
        if path.name in allowed_root_entries:
            continue
        if path.is_file() and path.suffix.lower() in {".md", ".txt"}:
            errors.append(f"{path}: documentation must be consolidated into README.md")

    return errors


def main() -> int:
    errors = validate_repository()
    if errors:
        print("Notebook validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Notebook validation passed: {len(iter_notebooks())} notebooks checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
