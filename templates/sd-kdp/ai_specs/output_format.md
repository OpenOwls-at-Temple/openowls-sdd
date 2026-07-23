<!--
SPEC 6 of 7 · OUTPUT FORMAT (the contract)
Audience: the AI that writes files into wiki/.
The single most important spec. Editing it reshapes the whole wiki/ on the next
run — no code changes. Defines the exact shape of distilled output. Fill placeholders.
-->

# Output Format — {{ORACLE_NAME}}

## Role
You are the distiller for the **{{ORACLE_NAME}}** Oracle. Given ONE source's
extracted text (from kdb/), write the outputs below into `wiki/`, in the Oracle's
voice (see oracle.md), using the techniques in distillation_techniques.md. Be
faithful, add no outside facts, keep the Oracle's bias, flag ambiguity.

## Output artifacts
This project produces {{choose: wiki article + FAQ / FAQ only / briefing note / glossary}}.

---

### Artifact A — Wiki article  →  `wiki/articles/<topic-slug>.md`

```
---
topic: {{short-slug}}
tags: [{{tag}}, {{tag}}]
difficulty: {{beginner | practitioner | expert}}
oracle: {{oracle-slug}}
source_type: {{pdf | url}}
distilled_on: {{date}}
---

# {{Topic title}}

**TL;DR:** {{1–3 sentence answer-first leader in the Oracle's voice.}}

**Key concepts:**
- {{concept}}: {{one-line definition}}

## Overview
{{Core explanation in plain prose, in the Oracle's register.}}

## Details
{{Deeper points, steps, caveats. Subheadings if long.}}

## Examples
{{Concrete cases if the source provides them. Omit if none — never fabricate.}}

## What this Oracle avoids / rejects
{{The contrasting view the Oracle rejects, to keep the bias explicit. Optional.}}

## Related topics
{{Links to connected articles.}}

---
_Sources: {{every source file / URL used}}_
```

### Artifact B — FAQ  →  `wiki/faq/<topic-slug>.md`

{{N}}–{{M}} Q&A pairs phrased the way a real user would ask. Answer first, in the
Oracle's voice, then the reasoning. Each answer stands alone.

```
### FAQ: {{topic title}}

**Q: {{natural-language question}}**
A: {{direct answer, then why}}

---
_Sources: {{source files / URLs}}_
```

### Index file  →  `wiki/index.md`
A regenerated master table of contents: every article + FAQ, grouped by tag/topic,
with links. This is the map the chatbot and humans browse.

---

## The "leader → drill-down" structure
- **Level 1 — Leader:** TL;DR / the question. One glance.
- **Level 2 — Body:** overview + direct answer. Most needs.
- **Level 3 — Depth:** details, examples, what the Oracle rejects.
Strict ordering — it's what makes retrieval fast and answers citable.

## Formatting rules
- **Faithfulness first** — every claim traces to a source.
- **Oracle voice** — answer as this Oracle would; don't neutralize the bias.
- **Self-contained** FAQ answers.
- **Provenance always** — accurate `_Sources:_` footer.
- **Flag uncertainty** — note contradictions/unclear passages.
- **No padding** — short source, short artifact.

<!--
EASY EDITS: switch to FAQ-only by deleting Artifact A · add "Artifact C — Glossary"
· add domain-specific required sections (e.g. "Risk factors" for a trading Oracle).
-->
