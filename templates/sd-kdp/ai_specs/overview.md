<!--
SPEC 1 of 7 · OVERVIEW
Audience: everyone (business sponsor view). The goal and overall idea.
Fill every {{placeholder}}; delete comments.
-->

# Overview — {{ORACLE_NAME}}

## Goal
{{One or two sentences: what this project is for. e.g. "Build a distilled,
queryable knowledge base of Warren Buffett's value-investing philosophy that
answers investor questions in his voice."}}

## The idea
{{2–4 sentences on how it works: an Oracle is chosen, its sources are collected
into kdb/, distilled overnight into wiki/, and served to a chatbot the next day.}}

## Who it's for
- **Users asking questions:** {{who queries the chatbot and their background}}
- **Maintainer:** {{who runs/tunes the pipeline}}

## What "done" looks like
{{The acceptance test: the chatbot answers the Oracle's key questions accurately,
in the Oracle's voice, sourced from the distilled base.}}

## Non-goals
- {{what this project deliberately does NOT do}}
- {{e.g. not real-time; not investment advice; not multi-oracle in v1}}

## Success metrics (optional)
- {{e.g. can answer the 5 key questions in oracle.md; retrieval latency < X; nightly run cost < Y}}

## High-level flow
```
kdb/ (collected sources) ──collect.py──▶ distill.py ──▶ wiki/ (distilled) ──build_index──▶ chatbot
                                   guided by ai_specs/*
```
