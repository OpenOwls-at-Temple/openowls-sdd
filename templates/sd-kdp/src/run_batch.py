"""Orchestrator — the nightly SD-KDP pipeline.

Runs the four stages in order and logs the result. Schedule this with cron,
Task Scheduler, or a scheduled task (see ai_specs/batch_process.md):

    python src/run_batch.py

A single failing stage is logged; backup still runs so data is protected.
"""
from __future__ import annotations

import traceback
from datetime import datetime

from paths import PROGRESS, STATE, ensure_dirs

import collect
import distill
import build_index
import backup


def _log(line: str) -> None:
    ensure_dirs()
    logfile = STATE / "runs" / f"{datetime.now():%Y-%m-%d_%H%M%S}.log"
    with logfile.open("a") as f:
        f.write(line + "\n")
    print(line)


def _append_run_log(row: str) -> None:
    """Insert one row at the top of progress.md's run-log table (most recent first)."""
    if not PROGRESS.exists():
        return
    lines = PROGRESS.read_text().splitlines()
    for i, line in enumerate(lines):
        if line.strip().startswith("| ---"):
            rest = lines[i + 1:]
            # Drop the scaffold's empty placeholder row the first time we write.
            if rest and set(rest[0].replace("|", "").split()) <= {"—", "-"}:
                rest = rest[1:]
            PROGRESS.write_text("\n".join(lines[: i + 1] + [row] + rest) + "\n")
            return
    _log("[run-log] no run-log table found in progress.md — skipped")


def _cell(value) -> str:
    """Render a stage result for a markdown table cell (no pipes allowed)."""
    if value is None:
        return "FAILED"
    return str(value).replace("|", "/")


def main() -> None:
    _log(f"=== SD-KDP run {datetime.now():%Y-%m-%d %H:%M:%S} ===")
    results: dict[str, dict | None] = {}
    for name, stage in (
        ("collect", collect.collect),
        ("distill", distill.distill),
        ("build_index", build_index.build_index),
    ):
        try:
            results[name] = stage()
            _log(f"[{name}] {results[name]}")
        except Exception:  # noqa: BLE001 — keep going so backup still runs
            results[name] = None
            _log(f"[{name}] FAILED\n{traceback.format_exc()}")

    # Always back up, even if an earlier stage failed.
    try:
        results["backup"] = backup.backup()
        _log(f"[backup] {results['backup']}")
    except Exception:  # noqa: BLE001
        results["backup"] = None
        _log(f"[backup] FAILED\n{traceback.format_exc()}")

    # One-row summary in progress.md's run log (see ai_specs/batch_process.md).
    coll, dist = results["collect"], results["distill"]
    sources_in = "FAILED" if coll is None else coll["new"] + coll["changed"]
    distilled_out = "FAILED" if dist is None else f"{dist['articles']} articles, {dist['faqs']} FAQs"
    failed = [name for name, res in results.items() if res is None]
    notes = f"stages failed: {', '.join(failed)}" if failed else "ok"
    _append_run_log(
        f"| {datetime.now():%Y-%m-%d} | nightly | {_cell(sources_in)} "
        f"| {_cell(distilled_out)} | {_cell(notes)} |"
    )


if __name__ == "__main__":
    main()
