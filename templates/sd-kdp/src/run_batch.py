"""Orchestrator — the nightly SD-KDP pipeline.

Runs the four stages in order and logs the result. Schedule this with cron,
Task Scheduler, or a scheduled task (see ai_specs/batch_process.md):

    python src/run_batch.py

A single failing stage is logged; backup still runs so data is protected.
"""
from __future__ import annotations

import traceback
from datetime import datetime

from paths import STATE, ensure_dirs

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


def main() -> None:
    _log(f"=== SD-KDP run {datetime.now():%Y-%m-%d %H:%M:%S} ===")
    for name, stage in (
        ("collect", collect.collect),
        ("distill", distill.distill),
        ("build_index", build_index.build_index),
    ):
        try:
            _log(f"[{name}] {stage()}")
        except Exception:  # noqa: BLE001 — keep going so backup still runs
            _log(f"[{name}] FAILED\n{traceback.format_exc()}")

    # Always back up, even if an earlier stage failed.
    try:
        _log(f"[backup] {backup.backup()}")
    except Exception:  # noqa: BLE001
        _log(f"[backup] FAILED\n{traceback.format_exc()}")

    # TODO: append a one-row summary to progress.md's run-log table.


if __name__ == "__main__":
    main()
