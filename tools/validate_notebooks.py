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

        # Rule 1: consecutive duplicate markdown cells.
        if cell_type == "markdown":
            normalized = text.strip()
            if normalized and previous_markdown_norm == normalized:
                errors.append(
                    f"{path}: cell {cell_index}: consecutive duplicate markdown cell"
                )
            previous_markdown_norm = normalized
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

    for path in sorted(ROOT.glob("*")):
        if path.name in {"README.md", "LICENSE", "requirements.txt", ".gitignore", ".github", "tools", "notebooks", ".git"}:
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
