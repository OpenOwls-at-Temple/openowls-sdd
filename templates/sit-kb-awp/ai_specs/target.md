<!--
SPEC 2 of 10 · TARGET
Owner: DOMAIN EXPERT
Consumed by: critic (error signal), answerer (what to optimize), orchestrator
(when to score).
The organizing principle of the whole workflow. The system is TARGET-ORIENTED:
collection, distillation, and critique all exist to close the gap between
measured performance and this file. "Self-improving" means exactly: the gap
between the KPMs below and their thresholds is the error signal the critic
converts into proposed changes. Fill every {{placeholder}}.
-->

# Target — {{ORACLE_NAME}}

## Target statement
{{One sentence, measurable in spirit: what this workflow must reliably do.
e.g. "Produce a question bank per lecture such that ≥80% of questions are
accepted by the instructor unedited, all traceable to lecture material."}}

## Key Performance Metrics (KPMs)

### Regression KPMs — scored automatically after every build
The fixed eval set. These are the workflow's unit tests: every nightly run is
scored against them, so any spec change shows up as a KPM move.
| # | KPM | How measured | Threshold |
| --- | --- | --- | --- |
| R1 | {{e.g. groundedness: % of claims traceable to a source span}} | {{automatic check}} | {{≥ X%}} |
| R2 | {{e.g. coverage: every key question in oracle.md answerable}} | {{eval-set run}} | {{100%}} |
| R3 | {{e.g. contract validity: output parses against output_format.md}} | {{schema check}} | {{100%}} |
| R4 | {{e.g. voice: sampled outputs match the Oracle's declared stance}} | {{LLM judge vs oracle.md}} | {{≥ X}} |

### Live KPMs — scored from real usage via the feedback log
| # | KPM | How measured | Verdict window | Threshold |
| --- | --- | --- | --- | --- |
| L1 | {{e.g. human acceptance rate of outputs, unedited}} | feedback verdicts | {{on review}} | {{≥ X%, rising}} |
| L2 | {{e.g. calibration: % of judgment calls confirmed by outcome}} | outcome data | {{e.g. 2 days–1 week — see the VERDICT CLOCK in domain_knowledge.md}} | {{≥ X%}} |

## The eval set
- **Seed:** the "key questions" in oracle.md — they are the initial regression set.
- **Growth rule:** {{when a live exchange exposes a gap, the critic proposes
  adding that question to the eval set — this is how the target itself learns
  what users actually need. Domain expert approves additions.}}
- **Location:** `.state/eval_set/` — versioned; every scored run records the
  eval-set version it ran against.

## Verdict windows
When does ground truth arrive for each judgment the system makes? (Derived from
the temporal profile in domain_knowledge.md — restate the operative choices.)
- {{judgment type}}: score after {{window}} using {{signal}}.
- {{e.g. "over-reaction call: score at T+5 trading days using price reversal;
  re-score at T+20 for the slow verdict."}}

## Track record
Every scored judgment is appended to `.state/track_record/` — never rewritten.
The KPM trend over rounds IS the self-improvement curve; if it isn't rising,
the loop is broken and that itself is a finding for the critic.

## Out-of-target guardrails
- {{claims the system must never make even if they would score well —
  e.g. "never presents output as investment advice"}}
- {{KPM gaming to watch for — e.g. shorter answers inflating acceptance rate}}
