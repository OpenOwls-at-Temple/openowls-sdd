<!--
SPEC 7 of 10 · OUTPUT FORMAT  (the contract)
Owner: SHARED CONTRACT — two sections, two owners:
  §A "What artifacts must contain"  → DOMAIN EXPERT (domain judgment)
  §B "How artifacts are encoded"    → AGENT DEVELOPER (wire format)
Consumed by: distiller (writes), indexer + answerer (read).
The single most important spec: editing it reshapes all output on the next run
with no code changes. Like an API contract in SDD — the business owner defines
semantics, the architect defines the wire format. Fill placeholders.
-->

# Output Format — {{ORACLE_NAME}}

## Role
You are the distiller for the **{{ORACLE_NAME}}** Oracle. Given source material
per the recipes in distillation_techniques.md, write the artifacts below, in
the Oracle's voice (oracle.md). Be faithful, add no outside facts, keep the
Oracle's declared bias, flag ambiguity.

---

## §A — What artifacts must contain   *(owner: domain expert)*

This project produces: {{choose/extend: wiki article + FAQ / quiz bank JSON /
study cards / dated assessment brief / glossary}}.

**Required content per artifact** (domain judgment — the "every question needs
a difficulty level" layer):
- {{e.g. every quiz question carries: difficulty, topic tag, source lecture ref}}
- {{e.g. every assessment carries: expectations vs. actuals, quality flags,
  judgment + confidence, reasoning}}
- {{e.g. every article carries: TL;DR leader, what-the-Oracle-rejects section}}

**The "leader → drill-down" structure** (applies to all prose artifacts):
- **Level 1 — Leader:** TL;DR / the direct answer. One glance.
- **Level 2 — Body:** overview + reasoning. Most needs.
- **Level 3 — Depth:** details, examples, what the Oracle rejects.
Strict ordering — it's what makes retrieval fast and answers citable.

---

## §B — How artifacts are encoded   *(owner: agent developer)*

### Artifact A — Wiki article  →  `wiki/articles/<topic-slug>.md`   [tier: durable]
```
---
topic: {{short-slug}}
tags: [{{tag}}]
difficulty: {{beginner | practitioner | expert}}
oracle: {{oracle-slug}}
tier: durable
source_type: {{pdf | url}}
distilled_on: {{date}}
valid_until: {{date | "slow-drift"}}      # from the temporal profile
---
# {{Topic title}}
**TL;DR:** {{1–3 sentence answer-first leader in the Oracle's voice.}}
## Overview
## Details
## Examples                {{omit if none — never fabricate}}
## What this Oracle avoids / rejects     {{optional; keeps bias explicit}}
## Related topics
---
_Sources: {{every source file / URL used}}_
```

### Artifact B — {{FAQ / quiz bank / study cards}}  →  `{{path}}`   [tier: {{durable|episodic}}]
{{Define the exact schema. For machine-ingested formats (e.g. a game app's bulk
upload), paste the JSON schema and REQUIRE per-item: id, source ref, topic tag,
difficulty — without id + source pointer, feedback can't route anywhere.}}
```
{{schema / template}}
```

### Artifact C — Dated assessment  →  `assessments/{{period}}/{{entity}}.md`   [tier: episodic]
{{Delete if no episodic tier.}}
```
---
entity: {{slug}}
period: {{e.g. 2026-Q2}}
assessed_on: {{date}}
tier: episodic            # snapshot — valid AS OF assessed_on, never updated
lens_version: {{git ref of ai_specs at run time}}
judgment: {{the call made}}
confidence: {{low | medium | high}}
verdict_due: {{date — from target.md's verdict window}}
---
{{§A's required assessment sections}}
---
_Sources: {{event artifacts + wiki articles used as lens}}_
```
Append-only: re-analysis creates a new file; old judgments are the track record.

### Index  →  `wiki/index.md` + `.index/`
Regenerated master ToC and retrieval index. MUST carry the tier tag and dates
so retrieval can filter: lens questions → durable tier; episode questions →
episodic tier, date-filtered. Never serve an expired `valid_until` as current.

---

## Formatting rules (both owners)
- **Faithfulness first** — every claim traces to a source.
- **Oracle voice** — don't neutralize the declared bias.
- **Self-contained** items — each stands alone.
- **Provenance always** — accurate `_Sources:_` footer.
- **Date honesty** — episodic content always framed "as of {{date}}".
- **Flag uncertainty** — note contradictions/unclear passages.
- **No padding** — short source, short artifact.
