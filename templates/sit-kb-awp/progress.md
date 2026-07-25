# progress.md — Session Memory

The pipeline and any AI assistant have no memory between sessions. This file is
read first every session and updated at the end of every session and every run.

## Current status
- **Project:** {{ORACLE_NAME}} — {{one-line target from target.md}}
- **Phase:** scaffolding / not yet running
- **Last run:** —
- **KPM snapshot:** — {{latest regression + live KPM values, once running}}

## Done
- Project scaffolded (folders, 10 specs, gitignore).

## In progress
- Fill in the `ai_specs/` files for this Oracle and Target.

## Blocked / open questions
- {{anything waiting on a decision — note WHO owns the decision (domain expert
  vs. agent developer), per the ownership table}}

## Pending critic proposals
| Date | Proposal | Touches (spec) | Approver | Status |
| --- | --- | --- | --- | --- |
| — | — | — | — | — |

## Next steps
1. Complete `target.md` (the target statement + KPMs) and `oracle.md` (lens + canon).
2. Complete `domain_knowledge.md` — especially the temporal profile table.
3. Complete `collection_techniques.md` (canon inventory + inbox monitor).
4. Implement `src/collect.py`, then `src/distill.py` (both verbs).
5. First manual end-to-end run on one source; score against the eval set.
6. Schedule the nightly run; enable the feedback log; first critic round.

## Run log (most recent first)
| Date | Run type | Sources in | Artifacts out | KPM delta | Notes |
| --- | --- | --- | --- | --- | --- |
| — | — | — | — | — | — |

## Applied spec changes (most recent first)
| Date | Spec | Change | Motivating feedback ids | Approved by |
| --- | --- | --- | --- | --- |
| — | — | — | — | — |
