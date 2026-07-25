<!--
SPEC 6 of 10 · DISTILLATION TECHNIQUES
Owner: AGENT DEVELOPER
Consumed by: distiller (src/distill.py).
Defines HOW raw kdb/ sources become knowledge. The exact OUTPUT SHAPE lives in
output_format.md — this file is about method.
BEYOND LITE SD-KDP: distillation has TWO VERBS, one per tier:
  1. SUMMARIZE  — canon → wiki/. Compress the Oracle's library into reference
     knowledge. Updated in place when the canon changes.
  2. APPLY      — inbox + wiki/ → assessments/. Analyze fresh episodic material
     THROUGH the distilled lens. The wiki is an INPUT here, not a sibling.
     Output is dated and append-only.
"Distill" is a broader verb than summarize: generating quiz questions from
lectures or judging an earnings report through a value lens are both
distillation — knowledge transformed into the target form. Fill placeholders.
-->

# Distillation Techniques — {{ORACLE_NAME}}

## Verb 1 — SUMMARIZE (canon → wiki/)
- **Primary approach:** {{extractive / abstractive / hybrid}} — {{why, tied to
  the Oracle's voice and audience}}
- **Reprocess trigger:** changed source hash → re-distill → REPLACE the article.
- **Never** route inbox material here: a summarized episode becomes undated
  "reference knowledge" that will be confidently retrieved, stale, years later.

## Verb 2 — APPLY (inbox + wiki/ → assessments/)
{{Delete if this project has no episodic tier.}}
- **Recipe:** for each inbox event: load relevant wiki/ articles (the lens) +
  the event's raw artifacts → produce one dated assessment per
  output_format.md's Artifact {{X}}.
- **Reprocess trigger:** spec/lens changes — an unchanged filing may be
  re-analyzed because the critic improved the lens. Re-runs create a NEW dated
  assessment (append-only; the track record in target.md depends on never
  overwriting old judgments).

## Techniques to apply
Turn on/off and configure. Remove what doesn't apply; add Oracle-specific ones.
- **Progressive summarization:** {{on/off}} — leader → body → depth layers.
- **Chain-of-density:** {{on/off}} — iteratively pack key entities into fixed length.
- **Q&A / assessment generation:** {{on/off}} — derive the target form (FAQ,
  quiz bank, study cards, judgment brief) from source knowledge.
- **Entity & claim extraction:** {{on/off}} — named entities, figures, claims.
- **Feynman / plain rewrite:** {{on/off}} — force simple explanation, expose gaps.
- **Comparative synthesis:** {{on/off}} — merge multiple sources per topic.
- **Stance reinforcement:** {{on/off}} — explicitly name what the Oracle
  rejects, to keep bias visible and resist drift toward consensus.
- **{{project-specific technique}}:** {{on/off}} — {{describe}}

## Merge & dedup policy
- {{merge into one article per topic / keep separate}}
- **Contradictions:** apply oracle.md bias rule; {{flag inline / footnote}}.

## Quality guardrails
- **Groundedness:** every claim/figure maps to a source span (regression KPM R1).
- **Faithfulness pass:** {{second LLM pass verifying output vs. source — on/off}}.
- **Voice check:** does output reflect the Oracle's declared lens, or has it
  drifted to generic consensus? Distill-of-distill and merge passes neutralize
  bias gradually — reject drift. (Regression KPM R4.)
- **Coverage check:** the eval set in target.md must be answerable after a run.
- **Calibration rubric:** {{if outputs carry difficulty/severity/confidence
  labels, define the rubric here — what "hard" or "high-confidence" means.
  This is the knob the critic tunes from feedback.}}

## Chunking & context strategy
- **Source chunk size:** {{tokens}} · **Overlap:** {{tokens}}.
- **Long-source handling:** {{map-reduce / full-context if it fits}}.

## Model choices
- **Distillation model:** {{model — quality-sensitive}}.
- **Merge/verify model:** {{model — can differ}}.
- **Embedding model:** {{model for the retrieval index}}.

## Cost & run controls
- **Reprocess policy:** per-verb triggers above; `--force` rebuilds all.
- **Per-run budget or cap:** {{optional}}.
