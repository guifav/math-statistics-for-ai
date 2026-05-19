#!/usr/bin/env python3
"""Execute notebooks in-place and produce a JSONL report.

Usage:
    python3 tools/run_notebooks.py [--module 00-matematica] [--timeout 900] [--single path/to.ipynb]

Writes one JSON line per notebook to .nb_run_report.jsonl with keys:
  path, status, duration_s, n_cells, n_errors, first_error.

A notebook is considered ok when nbclient finishes without raising,
even if individual cells stored errors (we let allow_errors handle them).
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


def execute_one(path: Path, timeout: int, allow_errors: bool) -> dict:
    started = time.monotonic()
    rec: dict = {"path": str(path.relative_to(ROOT)), "status": "unknown"}
    try:
        nb = nbformat.read(path, as_version=4)
        client = NotebookClient(
            nb,
            timeout=timeout,
            kernel_name="python3",
            allow_errors=allow_errors,
            resources={"metadata": {"path": str(path.parent)}},
        )
        client.execute()
        nbformat.write(nb, path)
        # Count cells + errors stored in outputs
        n_cells = sum(1 for c in nb.cells if c.cell_type == "code")
        n_errors = 0
        first_error = None
        for c in nb.cells:
            if c.cell_type != "code":
                continue
            for o in c.get("outputs", []) or []:
                if o.get("output_type") == "error":
                    n_errors += 1
                    if first_error is None:
                        first_error = f"{o.get('ename')}: {(o.get('evalue') or '')[:200]}"
        rec.update(status="ok", n_cells=n_cells, n_errors=n_errors, first_error=first_error)
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


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--module", help="restrict to module subdir, e.g. 00-matematica")
    ap.add_argument("--single", help="run a single notebook path")
    ap.add_argument("--timeout", type=int, default=900, help="per-cell timeout seconds")
    ap.add_argument(
        "--strict",
        action="store_true",
        help="stop on first cell error (default: allow_errors so the rest runs)",
    )
    ap.add_argument("--append", action="store_true", help="append to existing report")
    args = ap.parse_args()

    paths = discover(args.module, args.single)
    if not paths:
        print("no notebooks found", file=sys.stderr)
        return 1

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
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
