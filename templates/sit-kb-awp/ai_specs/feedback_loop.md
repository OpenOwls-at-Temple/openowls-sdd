<!--
SPEC 9 of 10 · FEEDBACK LOOP  (what makes the workflow SELF-IMPROVING)
Owner: SHARED CONTRACT — verdict vocabulary & failure taxonomy: DOMAIN EXPERT;
schema, triage mechanics, critic scheduling: AGENT DEVELOPER.
Consumed by: critic.
The control loop: target.md declares the goal, this spec closes the gap.
Human feedback + outcome data → error signal → critic → PROPOSED changes →
approval routed by spec ownership → next round. The critic proposes against
any spec but approval authority follows ownership — that is what keeps
"self-improving" from drifting into "self-redefining". Fill placeholders.
-->

# Feedback Loop — {{ORACLE_NAME}}

## Feedback sources
1. **Human-in-the-loop** — verdicts on exchanges/artifacts (schema below).
2. **Outcome data** — {{delete if none. Delayed ground truth the world provides
   — e.g. price drift scoring an over-reaction call, exam results scoring quiz
   quality. Collected automatically per target.md's verdict windows. This
   partially automates the loop: the world grades the calls, with a delay.}}

## Feedback record   *(schema: agent developer · vocabulary: domain expert)*
Append to `.state/feedback/{{date}}.jsonl`, keyed to an exchange or artifact id:
```json
{
  "ref_id": "{{exchange id or artifact item id}}",
  "ts": "{{iso timestamp}}",
  "by": "{{human | outcome-scorer}}",
  "verdict": "{{one of the controlled vocabulary below}}",
  "note": "{{free text — optional}}",
  "better_answer": "{{what it should have said — optional, gold for the critic}}"
}
```

## Verdict vocabulary & failure taxonomy   *(owner: domain expert)*
The verdict category matters more than the prose — each failure type ROUTES to
a different spec. Extend per project; keep the routing column honest.

| Verdict | Meaning | Routes to (spec the fix lives in) |
| --- | --- | --- |
| `good` | accept as-is | — (positive signal; feeds KPM L1) |
| `not-grounded` | content not in the canon / invented | distillation (guardrails) or collection (filtering) |
| `wrong-vs-source` | contradicts the source material | distillation_techniques.md (faithfulness) |
| `missing-knowledge` | canon lacks this — needs new sources | collection_techniques.md (inventory) / oracle.md canon (expert approval) |
| `not-retrieved` | knowledge exists in wiki/ but wasn't found | serving.md (retrieval) / output_format.md (index fields) |
| `off-voice` | generic consensus, lens neutralized | oracle.md adherence / distillation (stance reinforcement) |
| `mis-calibrated` | {{e.g. too easy / too hard / over-confident}} | distillation_techniques.md (calibration rubric) |
| `stale` | expired content served as current | output_format.md (dates) / serving.md (filtering) |
| `{{project-specific}}` | {{…}} | {{…}} |

## The critic   *(brief)*
**Runs:** {{after each round / weekly / when N feedback records accumulate}},
before the next build.
**Reads:** feedback log, KPM trend + track record (target.md), run log
(progress.md), current specs.
**Produces — proposals only, never direct edits:**
- new sources → additions to collection inventory or `kdb/canon/links/`
- spec diffs → concrete edits to any ai_specs/ file, with the feedback
  records that motivated each
- re-run orders → topics to re-distill / events to re-assess under a new lens
- eval-set additions → live questions that exposed gaps (target.md growth rule)
**Style:** pattern-level, not case-level — "80% of `mis-calibrated` flags are
recall questions on conceptual lectures" beats ten one-off fixes.

## Approval routing   *(follows spec ownership — see the guide's table)*
| Proposal touches | Approver | Ceremony |
| --- | --- | --- |
| Developer-owned specs (collection/distillation/batch mechanics) | agent developer | low — {{or auto-approve rules, e.g. retry counts, chunk sizes}} |
| Expert-owned specs (target, oracle, domain_knowledge, §A contracts) | domain expert | required — the critic must not quietly redefine the GOAL while improving the MEANS |
| Eval-set additions | domain expert | required |

## Loop hygiene
- Every applied proposal is logged in progress.md with its motivating feedback ids.
- After an applied change, the next KPM scores are compared against the
  previous round — a change that moves no KPM is a finding in itself.
- **Dedup against history:** track rejected proposals; don't re-propose them
  every round.
- **Golden rule inherited from SD-KDP:** fix specs, not outputs. Hand-editing one
  bad artifact fixes nothing; the next run regenerates it.
