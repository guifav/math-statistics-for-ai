#!/usr/bin/env python3
"""Strip outputs and execution_count from committed notebooks.

The validator (`tools/validate_notebooks.py`) refuses notebooks whose code
cells carry `outputs` or `execution_count`. Run this script before committing
to clear those fields in-place, preserving cell sources, metadata and tags.

Usage:
    python3 tools/strip_notebook_outputs.py            # clean all notebooks
    python3 tools/strip_notebook_outputs.py --check    # exit 1 if any dirty
    python3 tools/strip_notebook_outputs.py path1 path2  # clean specific files
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK_ROOT = ROOT / "notebooks"


def iter_notebooks() -> list[Path]:
    return sorted(NOTEBOOK_ROOT.rglob("*.ipynb"))


def strip_notebook(path: Path) -> bool:
    """Return True if the notebook was modified."""
    original = path.read_text(encoding="utf-8")
    nb = json.loads(original)
    changed = False
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "code":
            continue
        if cell.get("outputs"):
            cell["outputs"] = []
            changed = True
        if cell.get("execution_count") is not None:
            cell["execution_count"] = None
            changed = True
    if not changed:
        return False
    serialized = json.dumps(nb, indent=1, ensure_ascii=False)
    if not serialized.endswith("\n"):
        serialized += "\n"
    path.write_text(serialized, encoding="utf-8")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        help="Specific notebooks to clean (defaults to every notebook under notebooks/).",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Do not write; exit 1 if any notebook would be modified.",
    )
    args = parser.parse_args()

    targets = [p.resolve() for p in args.paths] if args.paths else iter_notebooks()
    if not targets:
        print("No notebooks found", file=sys.stderr)
        return 2

    dirty: list[Path] = []
    for path in targets:
        if not path.exists():
            print(f"missing: {path}", file=sys.stderr)
            return 2
        if args.check:
            nb = json.loads(path.read_text(encoding="utf-8"))
            for cell in nb.get("cells", []):
                if cell.get("cell_type") != "code":
                    continue
                if cell.get("outputs") or cell.get("execution_count") is not None:
                    dirty.append(path)
                    break
        else:
            if strip_notebook(path):
                dirty.append(path)

    if args.check:
        if dirty:
            print("Notebooks contain outputs/execution_count:")
            for path in dirty:
                print(f"- {path.relative_to(ROOT)}")
            return 1
        print(f"All {len(targets)} notebooks are clean")
        return 0

    if dirty:
        print(f"Cleaned {len(dirty)} notebook(s):")
        for path in dirty:
            print(f"- {path.relative_to(ROOT)}")
    else:
        print(f"All {len(targets)} notebooks already clean")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
