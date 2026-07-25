<!--
SPEC 10 of 10 · BATCH PROCESS
Owner: AGENT DEVELOPER
Consumed by: orchestrator (src/run_batch.py) + scheduler.
Defines the scheduled/unattended jobs, event-driven runs, and backup.
BEYOND LITE SD-KDP: two run types (nightly canon maintenance vs. event-driven episodic
runs) + the scoring & critic stages. Keep in sync with progress.md's run log.
-->

# Batch Process — {{ORACLE_NAME}}

## Run types
| Run | Trigger | Stages |
| --- | --- | --- |
| **Nightly maintenance** | cron {{02:00 local}} | monitor → collect(canon) → distill:SUMMARIZE → index → eval-score → backup |
| **Event run** | monitor detects event (per collection_techniques.md) | collect(inbox) → distill:APPLY → index → backup |
| **Verdict run** | verdict window elapses (target.md) | outcome-score pending judgments → append track record |
| **Critic run** | {{weekly / N feedback records}} | critic reads feedback + KPMs → proposals → (human approval) → mark re-runs |

## Stage table
| # | Stage | Script | Reads | Writes |
| --- | --- | --- | --- | --- |
| 1 | Monitor | `src/monitor.py` | collection_techniques.md (inbox query) | `.state/events/` |
| 2 | Collect | `src/collect.py` | collection spec, `.state/events/` | `kdb/canon/`, `kdb/inbox/` |
| 3 | Distill | `src/distill.py` | kdb/, distillation + output_format + oracle specs | `wiki/`, `assessments/` |
| 4 | Index | `src/build_index.py` | `wiki/`, `assessments/` | `.index/` |
| 5 | Serve/Log | `src/serve.py` (or external app) | `.index/`, serving.md | `.state/exchanges/` |
| 6 | Score | `src/score.py` | eval set, exchanges, outcomes, target.md | `.state/track_record/`, KPM log |
| 7 | Critic | `src/critic.py` | `.state/feedback/`, KPMs, specs | `proposals/` (pending approval) |
| 8 | Backup | `src/backup.py` | kdb/, wiki/, assessments/, .state/ | `backups/` (or cloud) |

## Schedule
- **Nightly:** {{cron / Task Scheduler / scheduled task}} → `python src/run_batch.py`
- **Event runs:** {{monitor as part of nightly + an intraday poll if the domain
  needs it — from the ARRIVAL clock in the temporal profile}}
- **Verdict runs:** driven by `verdict_due` dates in assessments/ front matter.

## Incremental behavior
- **Canon:** hash-based — only new/changed sources re-distilled. `--force` rebuilds.
- **Inbox:** event-based — new events analyzed once; re-analysis only on critic
  re-run orders (append-only output).

## Backup & retention  (kdb/, wiki/, assessments/ are NOT in git)
- **What:** full kdb/, wiki/, assessments/, `.state/` trees.
- **Where:** {{`backups/YYYY-MM-DD/` / cloud bucket / external drive}}.
- **How:** `src/backup.py` — {{timestamped copy / tar.gz / rsync / cloud sync}}.
- **Retention:** canon + wiki + assessments + track record: keep {{long}};
  raw inbox: prune after {{N periods}}; backups: keep {{N}} snapshots.
- **Restore:** {{one line on restoring a snapshot}}.

## Logging & alerting
- Each run appends a row to progress.md's run log (date, run type, counts, KPM
  deltas, notes). Detailed logs in `.state/runs/<timestamp>.log`.
- **On failure:** {{retry policy; notification channel}}.

## Failure isolation
- A single bad source must not abort the run; log and continue.
- If distillation fails for a topic, keep the previous wiki/ version.
- A failed event run is retried but ALSO logged as a missed window (time-critical).
- Critic proposals are never auto-applied to expert-owned specs (feedback_loop.md).
