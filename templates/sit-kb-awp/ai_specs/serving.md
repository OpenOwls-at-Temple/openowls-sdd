<!--
SPEC 8 of 10 · SERVING  (the answerer / front-end contract)
Owner: SHARED CONTRACT — answer semantics: DOMAIN EXPERT; exchange record &
retrieval mechanics: AGENT DEVELOPER.
Consumed by: answerer (the serving agent or external front-end).
The serving stage is where the workflow meets users — a chatbot, an app that
ingests the output (e.g. a quiz game), or a generated report. Its critical
duty besides answering: LOG A STRUCTURED EXCHANGE RECORD, because feedback
has nothing to attach to without one. Fill placeholders.
-->

# Serving — {{ORACLE_NAME}}

## Front-end type
{{chatbot over the index / external app ingesting artifacts / scheduled report}}
- If an EXTERNAL APP is the front-end, the serving contract collapses to:
  "produce valid artifacts the app ingests" (see output_format.md §B) and the
  exchange record is the app's usage/review session.

## Answer contract   *(owner: domain expert)*
- **Voice:** answer AS the Oracle (oracle.md) — persona adopted, bias declared.
- **Grounding rule:** answer ONLY from wiki/ + assessments/. If retrieval finds
  nothing sufficient: say so, in-voice — never fall back to generic model
  knowledge. (The whole point: the canon's boundary is the knowledge boundary.)
- **Citation rule:** every answer names its sources (article/assessment slugs).
- **Date honesty:** episodic answers framed "as of {{date}}"; expired
  `valid_until` content flagged, not asserted.
- **Compliance line:** {{e.g. "educational only, not investment advice" — from
  domain_knowledge.md}}
- **Answer shape:** {{leader → body → depth, or the app's required form}}

## Retrieval mechanics   *(owner: agent developer)*
- **Index:** `.index/` built by src/build_index.py over wiki/ + assessments/.
- **Tier routing:** lens/how-to questions → durable tier; what-happened
  questions → episodic tier, date-filtered. {{two indexes / one index + tier
  tag filter}}
- **Top-k / rerank:** {{settings}}
- **Fallback:** {{optional second tier over raw kdb/ spans, for detail the
  distillation dropped — cheap insurance against lossy compression}}

## Exchange record   *(owner: agent developer — REQUIRED)*
Append one record per exchange to `.state/exchanges/{{date}}.jsonl`:
```json
{
  "id": "{{uuid}}",
  "ts": "{{iso timestamp}}",
  "question": "…",
  "retrieved": ["{{slug}}", "{{slug}}"],
  "tier_used": "durable | episodic | both | none",
  "answer": "…",
  "sources_cited": ["…"],
  "eval_set_question": false
}
```
This record is the anchor for feedback_loop.md — verdicts attach to `id`.

## Eval-set runs
The regression KPMs in target.md are scored by running the eval set THROUGH
this same serving path (same retrieval, same contract), flagged
`eval_set_question: true`. Testing a different path than users experience
measures nothing.
