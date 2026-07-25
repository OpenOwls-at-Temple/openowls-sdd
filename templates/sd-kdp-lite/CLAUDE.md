# CLAUDE.md — entry point for AI sessions

This is an **SD-KDP Lite** project (the quick-start version of the
Spec-Driven Knowledge Distillation Process family): declare an Oracle,
distill its canon into a queryable wiki, serve it in the Oracle's voice,
improve the specs from feedback. The specs in `ai_specs/` are the source of
truth; `src/` merely executes them.

## Read order (every session)
1. `progress.md` — session memory: status, run log, open questions.
2. `ai_specs/overview.md` → `oracle.md` → `pipeline.md` → `loop.md`.

## Ground rules
- **Fix specs, not outputs** — hand-edited artifacts are regenerated away.
- **One lens** — keep the Oracle's declared bias; reject drift to consensus.
- **Trace every claim to a source**; provenance footer always.
- **Serve only from wiki/** — "not covered" beats improvising.
- **kdb/ and wiki/ contents stay out of git**; backed up by `src/backup.py`.
- **Update progress.md** every session and every run.

## The SD-KDP family (three versions)
- **SD-KDP Lite** (this): 4 merged specs — the quick start.
- **SD-KDP** (the original): 8 specs, one per concern — graduate there when
  the merged files get crowded and you want collection, distillation, output
  format, and measures as separate contracts.
- **SIT-KB-AWP**: 10 specs + agent roster — graduate there when a spec gains
  a **second owner** (approval routing between domain expert and agent
  developer) or a **second clock** (event-driven sources, dated append-only
  outputs, delayed verdict windows, a critic agent).
