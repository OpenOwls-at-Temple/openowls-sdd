# SD-KDP — Spec-Driven Knowledge Distillation Process

### *Learning From Your Oracle*

A spec-first scaffold for building an AI-powered knowledge digestion project. You
declare an **Oracle** — a perspective plus its trusted body of knowledge (a person
like Warren Buffett, an institution like the Fed, or a site/knowledge base) — write
seven small spec files, and the pipeline collects that Oracle's sources, distills
them overnight, and serves questions in the Oracle's voice.

The core idea: a generic LLM averages every viewpoint into bland consensus. SD-KDP
deliberately commits to **one lens** and its sources. That declared bias is the point.

## Method lineage
SD-KDP adapts Spec-Driven Development (specs first, in version control, used to
brief the AI) from building *software* to building *distilled knowledge*.

## Folder structure

```
sd-kdp/
├── CLAUDE.md                    ← entry point: read specs in order, then progress.md
├── progress.md                  ← living session status + run log
├── .gitignore                   ← ignores kdb/ and wiki/ CONTENTS (kept via .gitkeep)
├── README.md                    ← this file
│
├── ai_specs/                    ← the specs (source of truth, tracked in git)
│   ├── overview.md              ← 1. goal and overall idea
│   ├── domain_knowledge.md      ← 2. domain terminology, rules, constraints
│   ├── oracle.md                ← 3. which Oracle/guru to follow + intended bias
│   ├── collection_techniques.md ← 4. where & how documents are downloaded
│   ├── distillation_techniques.md ← 5. how knowledge is distilled
│   ├── output_format.md         ← 6. format of distilled output (wiki / FAQ)
│   └── batch_process.md         ← 7. batch/scheduled jobs + backup
│
├── kdb/                         ← collected raw documents (CONTENTS gitignored, backed up)
│   └── .gitkeep
├── wiki/                        ← distilled output (CONTENTS gitignored, backed up)
│   └── .gitkeep
└── src/                         ← Python for batch + compute jobs (tracked in git)
    ├── collect.py               ← downloads sources into kdb/
    ├── distill.py               ← distills kdb/ into wiki/ per the specs
    ├── build_index.py           ← builds the retrieval index over wiki/
    ├── backup.py                ← backs up kdb/ and wiki/
    └── run_batch.py             ← orchestrates the nightly pipeline
```

## Why kdb/ and wiki/ contents are gitignored
`kdb/` (collected documents) and `wiki/` (distilled output) change every day —
they're data, not code. Committing them would bloat the repo and churn diffs. So
the **folders are tracked** (via `.gitkeep`) but their **contents are not**.
Instead they're **backed up by the system**: `src/backup.py` snapshots both to
`backups/` (or a cloud target) on each run — see `ai_specs/batch_process.md`.

Only the specs (`ai_specs/`) and the code (`src/`) live in git. That's everything
needed to regenerate `kdb/` and `wiki/` from scratch.

## How to start a project
1. Fill in the seven `ai_specs/` files — start with `overview.md` and `oracle.md`.
2. Implement/adjust the `src/` scripts for your sources.
3. Run `python src/run_batch.py` once by hand to collect + distill + index + back up.
4. Schedule it nightly (cron / Task Scheduler / a scheduled task).
5. Query the distilled `wiki/` with your chatbot the next day.
6. Update `progress.md` after each session.
