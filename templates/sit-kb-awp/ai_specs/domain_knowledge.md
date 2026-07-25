<!--
SPEC 3 of 10 · DOMAIN KNOWLEDGE
Owner: DOMAIN EXPERT
Consumed by: distiller, critic (and collector via the temporal profile).
Terminology, rules, constraints — and BEYOND LITE SD-KDP: the temporal profile, the
domain's facts about time. Every downstream timing behavior (refresh cadence,
tier routing, retention, feedback scoring schedule) is DERIVED from the
temporal profile rather than hard-coded in scripts. Fill every {{placeholder}}.
-->

# Domain Knowledge — {{ORACLE_NAME}}

## Domain summary
{{2–4 sentences describing the subject area and its shape — enough that someone
new understands the landscape before reading a source.}}

## Temporal profile  (beyond lite SD-KDP — required)
Knowledge has a half-life. The Oracle's lens is the slow-moving part — it has
seen enough episodes that one more rarely changes it. The episodes themselves
expire fast. One row per information type; downstream specs consume columns:
collection_techniques.md derives refresh cadence from ARRIVAL, distillation and
output_format derive tier routing and date-stamping from VALIDITY, and
target.md / feedback_loop.md derive their scoring schedule from VERDICT DELAY.

| Information type | Tier | Arrival (how often new info appears) | Validity (how long it stays true) | Verdict delay (when ground truth arrives) |
| --- | --- | --- | --- | --- |
| {{Oracle methodology texts}} | canon | {{rare / once}} | {{years — slow drift}} | — |
| {{e.g. lecture materials}} | {{canon or inbox}} | {{weekly, in-semester}} | {{semester}} | {{human review, days}} |
| {{e.g. quarterly filings}} | inbox | {{quarterly, per entity, pre-announced}} | {{snapshot — dated forever}} | — |
| {{e.g. market reaction}} | inbox | {{event + following days}} | {{snapshot}} | {{2 days – 1 week}} |

The three clocks are different things — do not conflate them:
1. **Arrival clock** → drives collection scheduling.
2. **Validity clock** → drives tier routing, `valid_until` stamping, retrieval
   filtering, and retention.
3. **Verdict clock** → drives when the feedback loop may score a judgment.
   It is a parameter of the TARGET: a 2-day verdict window and a 3-month one
   define different systems.

## Key terminology
Terms the distiller must interpret correctly (and as THIS Oracle uses them).
- **{{term}}:** {{definition}}
- **{{term}}:** {{definition}}

## Business / domain rules
Facts and rules that are always true in this domain and shape correct output.
- {{rule / heuristic}}
- {{rule / heuristic}}

## Common pitfalls & misconceptions
Things sources (or readers) often get wrong — flag or correct during distillation.
- {{pitfall}}
- {{pitfall}}

## Entities that matter
People, institutions, products, or concepts worth tagging/extracting.
- {{entity}} — {{why it matters}}

## External dependencies / constraints
- **Legal/compliance notes:** {{e.g. "educational only, not advice" — must also
  appear in serving.md's answer contract}}
- **Known gaps:** {{topics the canon doesn't cover well}}
