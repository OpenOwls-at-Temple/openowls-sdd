<!--
SPEC 1 of 4 · OVERVIEW (goal + target)
The business-owner view: what this is for and how you'll know it's working.
Fill every {{placeholder}}; delete comments.
-->

# Overview — {{ORACLE_NAME}}

## Goal
{{One or two sentences: what this project is for. Lead with the outcome, e.g.
"Build a distilled, queryable knowledge base of Warren Buffett's
value-investing philosophy that answers investor questions in his voice."}}

## The idea
{{2–4 sentences: an Oracle is chosen (oracle.md), its sources are collected
into kdb/, distilled overnight into wiki/ (pipeline.md), and served to users —
with feedback recorded each round (loop.md).}}

## Who it's for
- **Users asking questions:** {{who consumes the output and their background}}
- **Maintainer:** {{who runs and tunes the pipeline}}

## Target & measures
{{The lightweight version of a target spec — three lines, not a framework:}}
- **Target statement:** {{one measurable sentence — e.g. "≥80% of generated
  outputs accepted by the maintainer unedited, all traceable to sources."}}
- **Check after every run:** {{e.g. the key questions in oracle.md are
  answerable; every claim has a source; output parses/renders correctly}}
- **Watch over rounds:** {{one number that should rise — e.g. acceptance rate,
  logged in progress.md. If it isn't rising, the loop is broken.}}

## Non-goals
- {{what this project deliberately does NOT do}}
- {{e.g. not real-time; not advice; not multi-oracle}}

## High-level flow
```
kdb/ (collected) ──collect──▶ distill ──▶ wiki/ (distilled) ──▶ index ──▶ users
                        guided by ai_specs/*                        │
        ▲                                                           ▼
        └────────── loop.md: feedback → spec fixes ◀── progress.md log
```
