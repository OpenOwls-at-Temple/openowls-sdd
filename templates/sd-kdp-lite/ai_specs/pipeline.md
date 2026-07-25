<!--
SPEC 3 of 4 · PIPELINE (collection + distillation + output format)
The engineer view: where sources come from, how they're distilled, and the
exact shape of what's written into wiki/. The output-format section is the
contract — editing it reshapes the whole wiki/ on the next run, no code
changes. Fill every {{placeholder}}.
-->

# Pipeline — {{ORACLE_NAME}}

## 1 · Collection  (→ kdb/)

### Source inventory (keep in sync with oracle.md's canon)
| Source | Type | Location / URL | Refresh | Notes |
| --- | --- | --- | --- | --- |
| {{name}} | {{pdf / url / feed}} | {{path or link}} | {{once / weekly}} | {{}} |
| {{name}} | {{}} | {{}} | {{}} | {{}} |

### How to download
- **PDFs:** {{copy from folder / download}} → `kdb/pdfs/`.
- **URL lists:** parse `.md` files in `kdb/links/`, fetch, extract readable
  text (strip nav/ads), save to `kdb/fetched/<slug>.md`.
- **Robots/ToS:** respect robots.txt and site terms; {{rate limit}}.
- **Filtering:** collect only canon-consistent sources; skip the "explicitly
  rejected" list — don't even store them.

### Freshness & dedup
- {{Most lite projects are evergreen: fetch once. If any source refreshes on a
  clock (weekly lectures, monthly updates), note its cadence in the inventory
  and date-stamp what it produces — knowledge has a half-life. If you find
  yourself needing event-driven collection and dated snapshot outputs, that's
  the graduation signal: move to SIT-KB-AWP.}}
- Hash collected docs in `.state/manifest.json`; skip unchanged; record every
  item's source URL/path for provenance.
- On fetch failure: retry {{N}}, log to progress.md, continue — never let one
  bad source abort the run.

## 2 · Distillation  (kdb/ → wiki/)

- **Approach:** {{extractive / abstractive / hybrid}} — {{why, tied to voice
  and audience}}.
- **Techniques on:** {{pick: progressive summarization (leader → body → depth)
  / Q&A generation / entity & claim extraction / plain rewrite / comparative
  synthesis / stance reinforcement (name what the Oracle rejects)}}.
- **Guardrails:** every claim maps to a source span; voice check — reject
  drift toward generic consensus; the key questions in oracle.md must be
  answerable after each run.
- **Chunking:** {{tokens}} with {{overlap}}; long sources: {{map-reduce /
  full-context}}.
- **Models:** distill {{model}}; embed/index {{model}}.
- **Reprocess:** hash-based — only new/changed sources; `--force` rebuilds.

## 3 · Output format  (the contract)

**Role:** You are the distiller for **{{ORACLE_NAME}}**. Given one source's
text, write the artifacts below in the Oracle's voice. Be faithful, add no
outside facts, keep the declared bias, flag ambiguity.

**This project produces:** {{wiki articles + FAQ / quiz-bank JSON / study
cards / briefing notes}}.

### Artifact — {{name}}  →  `wiki/{{path}}`
```
---
topic: {{slug}}
tags: [{{tag}}]
difficulty: {{level}}
oracle: {{oracle-slug}}
distilled_on: {{date}}
---
# {{Title}}
**TL;DR:** {{1–3 sentence answer-first leader in the Oracle's voice}}
## Overview        ← core explanation, Oracle's register
## Details         ← deeper points; subheadings if long
## Examples        ← only if the source provides them — never fabricate
---
_Sources: {{every source file / URL used}}_
```
{{For machine-ingested formats (e.g. a quiz app's bulk upload), paste the JSON
schema instead — and require per-item: id, source ref, topic tag, difficulty.
Without id + source pointer, feedback can't route anywhere.}}

### Index  →  `wiki/index.md`
Regenerated master ToC: every artifact, grouped by tag/topic, with links.

**Structure rule — leader → body → depth, strictly ordered:** the one-glance
answer first, the working explanation second, the depth last. It's what makes
retrieval fast and answers citable.

**Formatting rules:** faithfulness first · Oracle voice (don't neutralize the
bias) · self-contained items · provenance footer always · flag uncertainty ·
no padding.
