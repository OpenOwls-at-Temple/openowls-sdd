# SIT-KB-AWP — Self-Improving Target-oriented Knowledge-Based Agent Workflow Process

### *the full-scale extension of SD-KDP (Spec-Driven Knowledge Distillation Process)*

A spec-first scaffold for building a knowledge workflow that **improves itself
against a declared target**. You declare a **Target** (what the workflow must
reliably do, measured by KPMs), choose an **Oracle** (the lens and canon used
to hit it), fill in ten small spec files, and a team of simple agents —
collector, distiller, answerer, critic — runs the loop: collect, distill,
serve, score, critique, improve.

Two ideas carry over from SD-KDP unchanged: a generic LLM averages every
viewpoint into bland consensus, so we deliberately commit to **one declared
lens**; and the specs — not the code — are the source of truth, in git.

What SIT-KB-AWP adds over the lite SD-KDP: the **target-first control loop**
(KPMs and verdict windows as the error signal), a **critic agent** whose
proposals are gated by **spec ownership** (domain expert vs. agent developer),
the **two-tier / two-verb** knowledge model (durable canon vs. episodic inbox;
summarize vs. apply), and the **temporal profile** (arrival / validity /
verdict clocks declared as domain facts).

**Not sure you need all this?** SIT-KB-AWP is the largest of a three-version
family: start with **SD-KDP Lite** (four merged specs) or the original
**SD-KDP** (eight specs, one per concern, with `progress_measure.md` as its
lightweight measure-and-feedback spec) — and graduate here when a spec gains
a second owner or a second clock.

**Read the full guide:** [`index.md`](index.md) — concepts, agent roster,
ownership table, workflow steps, golden rules, and related work.

## Folder structure

```
sit-kb-awp/
├── CLAUDE.md                      ← entry point: read order + ground rules
├── progress.md                    ← session memory + run log + KPM snapshot
├── index.md                       ← the guide (GitHub Pages ready)
├── .gitignore                     ← ignores data folder CONTENTS (kept via .gitkeep)
│
├── ai_specs/                      ← the ten specs (source of truth, in git)
│   ├── overview.md                ← 1. goal & idea            (domain expert)
│   ├── target.md                  ← 2. KPMs & verdict windows (domain expert)
│   ├── domain_knowledge.md        ← 3. domain + temporal profile (domain expert)
│   ├── oracle.md                  ← 4. the lens & canon       (domain expert)
│   ├── collection_techniques.md   ← 5. two-tier collection    (agent developer)
│   ├── distillation_techniques.md ← 6. two verbs              (agent developer)
│   ├── output_format.md           ← 7. artifact contracts     (shared)
│   ├── serving.md                 ← 8. answerer + exchange log (shared)
│   ├── feedback_loop.md           ← 9. verdicts, critic, approvals (shared)
│   └── batch_process.md           ← 10. runs, schedule, backup (agent developer)
│
├── kdb/canon/                     ← durable library   (contents gitignored)
├── kdb/inbox/                     ← episodic mailroom (contents gitignored)
├── wiki/                          ← distilled lens — undated, updated in place
├── assessments/                   ← applied analyses — dated, append-only
└── src/                           ← monitor, collect, distill, index, serve,
                                     score, critic, backup, run_batch
```

## Quick start

1. Fill in `target.md` and `oracle.md` first — target before lens, lens before pipeline.
2. Complete the temporal profile in `domain_knowledge.md`.
3. Fill the remaining specs; implement/adjust `src/` for your sources.
4. Run once by hand; score against the eval set; fix specs, not outputs.
5. Schedule the nightly run; collect feedback; let the critic propose; approve
   per the ownership table.
6. Watch the KPM trend in `progress.md` — that curve is the self-improvement.
