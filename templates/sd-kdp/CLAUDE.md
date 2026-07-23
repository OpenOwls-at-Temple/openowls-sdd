# CLAUDE.md — SD-KDP Project Entry Point

This is a **Spec-Driven Knowledge Distillation Process (SD-KDP)** project. Before
doing any work, read the spec files below **in this order**, then read
`progress.md` to see where the project stands.

## Read first, in order
1. `ai_specs/overview.md` — the goal and overall idea of this project
2. `ai_specs/domain_knowledge.md` — domain terminology, rules, constraints
3. `ai_specs/oracle.md` — which Oracle (guru / institution / site) we follow, and the intended bias
4. `ai_specs/collection_techniques.md` — where and how source documents are downloaded into `kdb/`
5. `ai_specs/distillation_techniques.md` — how raw sources are distilled
6. `ai_specs/output_format.md` — the exact shape of distilled output written to `wiki/`
7. `ai_specs/batch_process.md` — the scheduled/batch jobs and backup
8. `progress.md` — living status: what's done, in progress, blocked

## What this project does
Collects source documents from an Oracle's canon into `kdb/`, distills them
overnight into `wiki/` in the format defined by `output_format.md`, and serves
questions from the distilled base — answering in the Oracle's voice, not a
generic averaged consensus.

## Folder rules
- `kdb/` — collected raw documents. **Contents are gitignored** (change daily); the folder is kept via `.gitkeep`.
- `wiki/` — distilled output. **Contents are gitignored** (regenerated daily); folder kept via `.gitkeep`.
- `src/` — all Python for the collection, distillation, indexing, and backup jobs. **Tracked in git.**
- `ai_specs/` — the specs. **Tracked in git. Source of truth.**
- `kdb/` and `wiki/` are backed up by `src/backup.py`, not by git.

## Behavior rules
- The spec files are the source of truth. If output looks wrong, fix the spec first, then re-run.
- Do not commit anything under `kdb/` or `wiki/`, and never commit secrets — use `.env`.
- Update `progress.md` at the end of every work session; the next session starts from it.
- Preserve the Oracle's declared bias — do not neutralize distilled answers into generic consensus.
