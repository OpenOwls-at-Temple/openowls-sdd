<!--
SPEC 7 of 7 · BATCH PROCESS
Audience: DevOps/engineer + the orchestrator (src/run_batch.py).
Defines the scheduled/unattended jobs and the backup of kdb/ and wiki/.
Keep this in sync with progress.md's run log. Fill placeholders.
-->

# Batch Process — {{ORACLE_NAME}}

## The nightly pipeline
Runs unattended (e.g. 02:00). Orchestrated by `src/run_batch.py`, which calls the
stages in order and logs each to `progress.md` and `.state/runs/`.

| # | Stage | Script | Reads | Writes |
| --- | --- | --- | --- | --- |
| 1 | Collect | `src/collect.py` | collection_techniques.md, `kdb/links/` | `kdb/` |
| 2 | Distill | `src/distill.py` | `kdb/`, distillation_techniques.md, output_format.md, oracle.md | `wiki/` |
| 3 | Index | `src/build_index.py` | `wiki/` | `.index/` |
| 4 | Backup | `src/backup.py` | `kdb/`, `wiki/` | `backups/` (or cloud) |

## Schedule
- **Cadence:** {{e.g. daily at 02:00 local}}
- **Mechanism:** {{cron / Task Scheduler / a scheduled task / workflow runner}}
- **Trigger command:** `python src/run_batch.py`

## Incremental behavior
- Collect and distill are **hash-based**: only new/changed sources are reprocessed
  (see collection_techniques.md and distillation_techniques.md). `--force` rebuilds all.

## Backup of kdb/ and wiki/  (these are NOT in git)
Because `kdb/` and `wiki/` contents are gitignored and change daily, the batch
process is responsible for backing them up.
- **What:** the full `kdb/` and `wiki/` trees.
- **Where:** {{`backups/YYYY-MM-DD/` locally / cloud bucket / external drive}}.
- **How:** `src/backup.py` — {{timestamped copy / tar.gz / rsync / cloud sync}}.
- **Retention:** keep {{N}} days/versions; prune older.
- **Restore:** {{one line on how to restore a snapshot into kdb/ and wiki/}}.

## Logging & alerting
- Each run appends a row to `progress.md`'s run log (date, job, counts, notes).
- Detailed logs in `.state/runs/<timestamp>.log`.
- **On failure:** {{retry policy; how you're notified — e.g. email/Slack, optional}}.

## Failure isolation
- A single bad source must not abort the run; log it and continue.
- If distillation fails for a topic, keep the previous `wiki/` version for that topic.
