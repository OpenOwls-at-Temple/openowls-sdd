# SD-KDP Lite — Spec-Driven Knowledge Distillation Process

### *Learning From Your Oracle — the quick-start version*

A spec-first scaffold for building an AI-powered knowledge distillation
project — the **lite version** of the SD-KDP family: four small spec files,
one maintainer, a simple feedback loop. You declare an **Oracle** — a perspective plus its
trusted body of knowledge (a person like Warren Buffett, an institution like
the Fed, a site, or simply the scope of one professor's course) — and the
pipeline collects that Oracle's sources, distills them overnight, and serves
questions in the Oracle's voice.

The core idea: a generic LLM averages every viewpoint into bland consensus.
SD-KDP deliberately commits to **one lens** and its sources. That declared
bias is the point — and it lives in version control, where it's transparent.

## Method lineage
SD-KDP adapts Spec-Driven Development (specs first, in version control, used
to brief the AI) from building *software* to building *distilled knowledge*.

## Folder structure

```
sd-kdp/
├── CLAUDE.md              ← entry point: read order + ground rules
├── progress.md            ← session memory + run log + feedback table
├── .gitignore             ← ignores kdb/ and wiki/ CONTENTS (kept via .gitkeep)
│
├── ai_specs/              ← the four specs (source of truth, in git)
│   ├── overview.md        ← 1. goal + target & measures
│   ├── oracle.md          ← 2. the lens, canon, voice, key questions
│   ├── pipeline.md        ← 3. collection + distillation + output contract
│   └── loop.md            ← 4. serving + feedback + schedule & backup
│
├── kdb/                   ← collected raw sources   (contents gitignored)
├── wiki/                  ← distilled output        (contents gitignored)
└── src/                   ← collect, distill, build_index, backup, run_batch
```

## How to start
1. Fill in `overview.md` and `oracle.md` — goal and lens first.
2. Fill in `pipeline.md` (sources + output contract) and `loop.md`.
3. Implement/adjust `src/` for your sources; run once by hand.
4. Check the Oracle's key questions; **fix specs, not outputs**; re-run.
5. Schedule it nightly; record feedback verdicts; watch your target number
   rise across rounds in `progress.md`.

## The SD-KDP family — three versions

This is the smallest of three siblings:

| Version | Specs | For |
| --- | --- | --- |
| **SD-KDP Lite** (this) | 4 merged | learn the method in an afternoon; small static-corpus projects |
| **SD-KDP** (the original) | 8 | the reference version: a dedicated spec file per concern (collection, distillation, output format, batch, measures), one maintainer |
| **SIT-KB-AWP** | 10 + agent roster | the full self-improving agent workflow: monitor/collector/distiller/answerer/scorer/critic, two-tier temporal knowledge, outcome-scored judgments, ownership-gated approvals |

Two graduation rules:

- **Lite → SD-KDP** when merged files get crowded — you want collection,
  distillation, the output contract, and the measures each in its own file.
- **Anything → SIT-KB-AWP** when a spec gains a **second owner** (domain
  expert vs. agent developer needing approval routing) or a **second clock**:
  sources arriving on the world's schedule needing dated, append-only
  outputs; judgments scored by delayed ground truth (verdict windows); or a
  critic agent proposing spec edits instead of you making them.

Until either rule fires, four files are enough.
