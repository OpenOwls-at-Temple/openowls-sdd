<!--
SPEC 1 of 10 · OVERVIEW
Owner: DOMAIN EXPERT (business-owner view)
Consumed by: all agents (shared context) + every human on the project.
The goal and overall idea. Fill every {{placeholder}}; delete comments.
-->

# Overview — {{ORACLE_NAME}}

> **Framework:** SIT-KB-AWP — *Self-Improving Target-oriented Knowledge-Based
> Agent Workflow Process — the full-scale extension of SD-KDP*

## Goal
{{One or two sentences: what this workflow exists to produce. Lead with the
TARGET, not the mechanism. e.g. "Generate a review-session question bank from
this course's lecture materials, at calibrated difficulty, covering only what
the professor taught." The measurable version of this goal lives in target.md.}}

## The idea
{{2–4 sentences on how it works: a Target is declared (target.md), an Oracle is
chosen as the lens (oracle.md), its sources are collected into kdb/, distilled
into wiki/ and applied to fresh material in assessments/, served through a
front-end, and improved every round by a critic reading feedback against the
Target.}}

## Who is involved
- **Users:** {{who consumes the served output and their background}}
- **Domain expert:** {{who owns the goal-side specs — overview, target,
  domain_knowledge, oracle — and approves goal-level changes}}
- **Agent developer:** {{who owns the means-side specs — collection,
  distillation, batch — and implements src/}}

## What "done" looks like (v1 acceptance)
{{The first acceptance test in one paragraph. The ongoing, measurable version
is target.md's KPMs — this is just the "we can ship v1" bar.}}

## Non-goals
- {{what this project deliberately does NOT do}}
- {{e.g. not real-time; not advice; not multi-oracle in v1}}

## High-level flow
```
                     ai_specs/* (source of truth)
                              │ guides
        ┌─────────────────────┼──────────────────────┐
        ▼                     ▼                      ▼
kdb/canon/  ──distill──▶  wiki/  ──apply──▶  assessments/
kdb/inbox/  ─────────────────────────┘               │
   ▲                                                 ▼
collector ◀── critic ◀── feedback log ◀── answerer/front-end ◀── users
                │
                └── proposed spec diffs (approval follows ownership)
```
