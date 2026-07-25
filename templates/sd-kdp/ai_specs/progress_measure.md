<!--
SPEC 8 of 8 · PROGRESS MEASURE
Audience: the maintainer + any AI session reviewing results.
Defines how this project measures its own performance: the target, the checks
after every run, and how feedback routes to spec fixes. Companion to
progress.md — progress.md LOGS what happened; this spec defines WHAT to
measure and WHERE each kind of failure gets fixed.
Fill every {{placeholder}}; delete comments.
-->

# Progress Measure — {{ORACLE_NAME}}

## Target
- **Target statement:** {{one measurable sentence — e.g. "≥80% of distilled
  outputs accepted by the maintainer unedited, every claim traceable to a
  source."}}
- **Trend number:** {{the ONE number to watch across rounds — e.g. acceptance
  rate. Recorded in progress.md after each review. If it isn't rising over
  rounds, the loop is broken — and that itself is a finding.}}

## Checks after every run
Re-verify these before trusting a fresh `wiki/`:
- The **key questions** in oracle.md are answerable from the distilled base.
- Every claim/figure carries a **source** (provenance footer present, accurate).
- Output **matches the contract** in output_format.md (parses/renders; required
  fields present).
- Spot-check **voice**: still the Oracle's declared lens, not generic consensus.
- {{project-specific check}}

## Feedback verdicts
After using or reviewing output, record one line per item in
{{`.state/feedback.md` / a table in progress.md}}:

| Date | Item | Verdict | Note |
| --- | --- | --- | --- |
| {{}} | {{artifact / question}} | {{see vocabulary}} | {{}} |

**Verdict vocabulary — each type routes to the spec where the fix lives:**
- `good` — accept as-is (counts toward the trend number)
- `not-grounded` — invented content → distillation_techniques.md (guardrails)
- `wrong-vs-source` — contradicts the source → distillation_techniques.md (faithfulness)
- `missing-knowledge` — canon lacks it → collection_techniques.md (source inventory)
- `not-retrieved` — exists in wiki/ but not found → output_format.md (index/structure)
- `off-voice` — drifted to generic consensus → oracle.md adherence
- `mis-calibrated` — {{e.g. too easy / too hard / overconfident}} → distillation_techniques.md ({{rubric}})
- `{{project-specific}}` — {{…}} → {{…}}

## Review cadence
- {{Weekly / after each round}}: read the feedback table, find the *pattern*
  (not the one-off), make the spec edit, note it in progress.md, re-run.
- **Golden rule: fix specs, not outputs** — a hand-edited artifact is
  regenerated away on the next run.

<!--
NOTE: this is the lightweight measure spec. If you need automated eval-set
scoring, delayed outcome-based verdicts (e.g. market reaction windows), or a
critic agent proposing spec diffs under approval routing — graduate to
SIT-KB-AWP, where this file's job splits into target.md + feedback_loop.md.
-->
