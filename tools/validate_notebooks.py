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

    for cell_index, cell in enumerate(cells, start=1):
        text = source_text(cell)
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
        if cell.get("cell_type") != "code" or not should_parse_python(text):
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
