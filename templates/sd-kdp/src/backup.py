"""Stage 4 — Backup.

kdb/ and wiki/ contents are gitignored (they change daily), so the batch process
backs them up here instead of git. See ai_specs/batch_process.md.

Default: a timestamped tar.gz of kdb/ and wiki/ into backups/. Swap in rsync or a
cloud sync (S3/GCS/Drive) by editing snapshot().

This is a STUB you can run as-is for local snapshots.
"""
from __future__ import annotations

import tarfile
from datetime import datetime

from paths import KDB, WIKI, BACKUPS, ensure_dirs

RETENTION = 14  # keep this many snapshots


def snapshot() -> str:
    """Create a timestamped tar.gz of kdb/ and wiki/. Returns the archive path."""
    ensure_dirs()
    stamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    archive = BACKUPS / f"sd-kdp_{stamp}.tar.gz"
    with tarfile.open(archive, "w:gz") as tar:
        tar.add(KDB, arcname="kdb")
        tar.add(WIKI, arcname="wiki")
    return str(archive)


def prune(keep: int = RETENTION) -> int:
    """Delete old snapshots beyond `keep`. Returns count removed."""
    snaps = sorted(BACKUPS.glob("sd-kdp_*.tar.gz"))
    removed = 0
    for old in snaps[:-keep] if keep else []:
        old.unlink()
        removed += 1
    return removed


def backup() -> dict:
    path = snapshot()
    return {"archive": path, "pruned": prune()}


if __name__ == "__main__":
    print(backup())
