<!--
SPEC 4 of 4 · LOOP (serving + feedback + schedule)
How the output reaches users, how feedback comes back, and when things run.
This is the lightweight loop: one human, simple verdicts, spec fixes by hand.
If you need outcome-based scoring, a critic agent, or approval routing between
multiple owners — that's the graduation signal: move to SIT-KB-AWP.
Fill every {{placeholder}}.
-->

# Loop — {{ORACLE_NAME}}

## 1 · Serving

- **Front-end:** {{chatbot over the index / an app that ingests the artifacts
  (e.g. quiz game) / a generated report}}.
- **Grounding rule:** answer ONLY from wiki/. If nothing sufficient is
  retrieved: say "not covered", in-voice — never fall back to generic model
  knowledge. The canon's boundary is the knowledge boundary; that's the point.
- **Citation rule:** every answer names its sources.
- **Voice:** answer AS the Oracle (oracle.md). {{Compliance line, if any.}}
- **Keep a trace:** {{minimal exchange log — date, question, answer, sources
  cited — a jsonl file or even a table in progress.md. Feedback needs
  something to point at.}}

## 2 · Feedback

After using the output (or reviewing a batch), record verdicts — one line
each, in `{{.state/feedback.md or jsonl}}`:

| Date | Item (id/question) | Verdict | Note |
| --- | --- | --- | --- |
| {{}} | {{}} | {{good / not-grounded / wrong-vs-source / missing-knowledge / not-retrieved / off-voice / mis-calibrated}} | {{}} |

The verdict matters more than the note — each type routes to a fix:
- `not-grounded` / `wrong-vs-source` → pipeline.md §2 guardrails
- `missing-knowledge` → pipeline.md §1 inventory (new sources)
- `not-retrieved` → pipeline.md §3 index/format
- `off-voice` → oracle.md adherence
- `mis-calibrated` {{e.g. too easy/hard}} → pipeline.md §2 {{rubric}}

**Golden rule: fix specs, not outputs.** A hand-edited artifact is regenerated
away on the next run. Review the feedback table {{weekly / each round}}, make
the spec edits, note them in progress.md, re-run — and watch the one number
from overview.md's target move.

## 3 · Schedule & backup

| # | Stage | Script | Writes |
| --- | --- | --- | --- |
| 1 | Collect | `src/collect.py` | `kdb/` |
| 2 | Distill | `src/distill.py` | `wiki/` |
| 3 | Index | `src/build_index.py` | `.index/` |
| 4 | Backup | `src/backup.py` | `backups/` |

- **Cadence:** {{nightly at 02:00 / weekly / manual}} via {{cron / Task
  Scheduler / scheduled task}} → `python src/run_batch.py`.
- **Backup:** kdb/ and wiki/ contents are gitignored (data, not code) — so
  `src/backup.py` snapshots both to {{backups/ / cloud}}; keep {{N}} versions.
- **Logging:** each run appends a row to progress.md's run log; a single bad
  source never aborts the run.
