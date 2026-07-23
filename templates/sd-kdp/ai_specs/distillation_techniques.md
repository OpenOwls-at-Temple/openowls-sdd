<!--
SPEC 5 of 7 · DISTILLATION TECHNIQUES
Audience: engineer + the distill job (src/distill.py).
Defines HOW raw kdb/ sources are turned into distilled knowledge. The exact
OUTPUT SHAPE lives in output_format.md — this file is about method. Fill placeholders.
-->

# Distillation Techniques — {{ORACLE_NAME}}

## Summarization strategy
- **Primary approach:** {{extractive / abstractive / hybrid}}
- **Why:** {{tie to the Oracle's voice and audience}}

## Techniques to apply
Turn on/off and configure. Remove what doesn't apply; add Oracle-specific ones.
- **Progressive summarization:** {{on/off}} — layer output leader → body → depth (maps to output_format.md).
- **Chain-of-density:** {{on/off}} — iteratively pack key entities into a fixed length.
- **Q&A generation:** {{on/off}} — derive FAQ by imagining real user questions.
- **Entity & claim extraction:** {{on/off}} — pull named entities, figures, discrete claims.
- **Feynman / plain rewrite:** {{on/off}} — force simple explanation, expose gaps.
- **Comparative synthesis:** {{on/off}} — merge multiple sources per topic, don't repeat.
- **Stance reinforcement:** {{on/off}} — explicitly name what the Oracle rejects, to keep bias visible.
- **{{project-specific technique}}:** {{on/off}} — {{describe}}

## Merge & dedup policy
- {{merge into one article per topic / keep separate}}.
- **Dedup questions:** {{semantic match; keep clearest phrasing}}.
- **Contradictions:** apply oracle.md bias rule (prefer the Oracle's view) and {{flag inline / footnote}}.

## Quality guardrails
- **Hallucination check:** every claim/figure must map to a source span.
- **Faithfulness pass:** {{second LLM pass verifying output vs. source — on/off}}.
- **Voice check:** does output reflect the Oracle's declared philosophy, or has it drifted to generic consensus? Reject drift.
- **Coverage check:** the key questions in oracle.md must be answerable after a run.
- **Reading-level check:** {{target readability, if any}}.

## Chunking & context strategy
- **Source chunk size:** {{tokens}} · **Overlap:** {{tokens}}.
- **Long-source handling:** {{map-reduce / full-context if it fits}}.

## Model choices
- **Distillation model:** {{model — quality-sensitive}}.
- **Merge/verify model:** {{model — can differ}}.
- **Embedding model:** {{model for the retrieval index}}.

## Cost & run controls
- **Reprocess policy:** {{hash-based, only changed sources / full rebuild}}.
- **Per-run budget or cap:** {{optional}}.
