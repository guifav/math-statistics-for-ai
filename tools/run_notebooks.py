#!/usr/bin/env python3
"""Execute notebooks in-place and produce a JSONL report.

Usage:
    python3 tools/run_notebooks.py [--module 00-matematica] [--timeout 900] [--single path/to.ipynb]

Writes one JSON line per notebook to .nb_run_report.jsonl with keys:
  path, status, duration_s, n_cells, n_errors, first_error.

Exit codes:
  0  all notebooks finished (errors inside cells are tolerated by default)
  1  --strict mode AND at least one notebook had an error (cell error,
     execution exception, or stored error output)
  2  CLI error (no notebooks found, bad path, etc.)

Cells tagged `exercise` (without `solution`) are executed but errors inside
them do not count toward n_errors / strict mode — they are student scaffolds
that may have `TAREFA DO ALUNO` placeholders. This matches the repo contract
where `solution`-tagged cells carry the working code that must execute cleanly.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
import traceback
from pathlib import Path

import nbformat
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError


class _ScaffoldTolerantClient(NotebookClient):
    """NotebookClient subclass that lets errors raise in scaffold cells
    (tag `exercise` without `solution`) but does not propagate them. Solution
    and untagged cells use the standard behaviour controlled by `allow_errors`.

    nbclient honours `cell.metadata.tags` containing `raises-exception` to
    allow errors per-cell. We attach that tag at runtime to scaffold cells so
    the rest of the notebook keeps running even under `allow_errors=False`."""

    async def async_execute_cell(
        self, cell, cell_index, execution_count=None, store_history=True
    ):
        tags = (cell.metadata or {}).get("tags") or []
        scaffold = (
            cell.cell_type == "code"
            and "exercise" in tags
            and "solution" not in tags
        )
        if scaffold and "raises-exception" not in tags:
            cell.metadata.setdefault("tags", []).append("raises-exception")
        try:
            return await super().async_execute_cell(
                cell, cell_index, execution_count=execution_count, store_history=store_history
            )
        finally:
            if scaffold:
                # Leave the source/outputs alone but undo the runtime-only tag
                new_tags = [t for t in (cell.metadata.get("tags") or []) if t != "raises-exception"]
                cell.metadata["tags"] = new_tags


ROOT = Path(__file__).resolve().parents[1]
NB_ROOT = ROOT / "notebooks"
REPORT = ROOT / ".nb_run_report.jsonl"


def discover(module: str | None = None, single: str | None = None) -> list[Path]:
    if single:
        return [Path(single).resolve()]
    base = NB_ROOT if module is None else NB_ROOT / module
    if not base.exists():
        print(f"path not found: {base}", file=sys.stderr)
        return []
    return sorted(base.rglob("*.ipynb"))


def _is_exercise_only(cell) -> bool:
    """True when cell has tag `exercise` and not `solution`. These hold
    student scaffolds (TAREFA DO ALUNO) and must not be executed."""
    tags = (cell.get("metadata") or {}).get("tags") or []
    return "exercise" in tags and "solution" not in tags


def execute_one(path: Path, timeout: int, allow_errors: bool) -> dict:
    started = time.monotonic()
    rec: dict = {"path": str(path.relative_to(ROOT)), "status": "unknown"}
    try:
        nb = nbformat.read(path, as_version=4)

        n_scaffold = sum(1 for c in nb.cells if c.cell_type == "code" and _is_exercise_only(c))

        client = _ScaffoldTolerantClient(
            nb,
            timeout=timeout,
            kernel_name="python3",
            allow_errors=allow_errors,
            resources={"metadata": {"path": str(path.parent)}},
        )
        client.execute()
        nbformat.write(nb, path)

        n_cells = sum(1 for c in nb.cells if c.cell_type == "code")
        n_errors = 0
        scaffold_errors = 0
        first_error = None
        for c in nb.cells:
            if c.cell_type != "code":
                continue
            for o in c.get("outputs", []) or []:
                if o.get("output_type") == "error":
                    if _is_exercise_only(c):
                        scaffold_errors += 1
                    else:
                        n_errors += 1
                        if first_error is None:
                            first_error = f"{o.get('ename')}: {(o.get('evalue') or '')[:200]}"
        rec.update(
            status="ok",
            n_cells=n_cells,
            n_errors=n_errors,
            first_error=first_error,
            scaffold_cells=n_scaffold,
            scaffold_errors=scaffold_errors,
        )
    except CellExecutionError as exc:
        rec.update(status="cell_error", first_error=str(exc)[:500])
    except Exception as exc:
        rec.update(
            status="exception",
            first_error=f"{type(exc).__name__}: {exc}"[:500],
            traceback=traceback.format_exc(limit=4),
        )
    rec["duration_s"] = round(time.monotonic() - started, 2)
    return rec


def _record_is_failure(rec: dict) -> bool:
    if rec.get("status") != "ok":
        return True
    return bool(rec.get("n_errors") or 0)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--module", help="restrict to module subdir, e.g. 00-matematica")
    ap.add_argument("--single", help="run a single notebook path")
    ap.add_argument("--timeout", type=int, default=900, help="per-cell timeout seconds")
    ap.add_argument(
        "--strict",
        action="store_true",
        help="(1) tell nbclient to raise on first cell error and (2) exit 1 if any notebook had errors",
    )
    ap.add_argument("--append", action="store_true", help="append to existing report")
    args = ap.parse_args()

    paths = discover(args.module, args.single)
    if not paths:
        print("no notebooks found", file=sys.stderr)
        return 2

    failed_in_strict: list[str] = []
    mode = "a" if args.append else "w"
    with REPORT.open(mode) as fh:
        for p in paths:
            print(f">> {p.relative_to(ROOT)}", flush=True)
            rec = execute_one(p, timeout=args.timeout, allow_errors=not args.strict)
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
            fh.flush()
            tag = "OK" if rec["status"] == "ok" and (rec.get("n_errors") or 0) == 0 else rec["status"].upper()
            extra = ""
            if rec.get("n_errors"):
                extra = f"  errors={rec['n_errors']}  first={rec.get('first_error')!r}"
            print(f"   {tag}  ({rec['duration_s']}s){extra}", flush=True)
            if args.strict and _record_is_failure(rec):
                failed_in_strict.append(rec["path"])

    if args.strict and failed_in_strict:
        print(
            f"\n--strict: {len(failed_in_strict)} notebook(s) with errors: "
            + ", ".join(failed_in_strict),
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
