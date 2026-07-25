# CLAUDE.md — entry point for AI sessions

This is a **SIT-KB-AWP** project (Self-Improving Target-oriented
Knowledge-Based Agent Workflow Process — the full-scale extension of SD-KDP).
The specs in `ai_specs/` are the source of truth; the code in `src/` merely
executes them.

## Read order (every session)
1. `progress.md` — session memory: current status, run log, open questions.
2. `ai_specs/overview.md` → `target.md` → `domain_knowledge.md` → `oracle.md`
   (the goal side, owned by the domain expert).
3. `ai_specs/collection_techniques.md` → `distillation_techniques.md` →
   `output_format.md` → `serving.md` → `feedback_loop.md` → `batch_process.md`
   (the means side + shared contracts).

## Ground rules
- **Fix specs, not outputs.** A bad artifact means a spec (or its execution) is
  wrong; hand-editing the artifact fixes nothing — the next run regenerates it.
- **Approval follows ownership.** Each spec's header names its owner. Propose
  diffs to expert-owned specs (target, oracle, domain_knowledge, §A contracts);
  never apply them without the domain expert's sign-off.
- **Two tiers, two verbs.** `kdb/canon/` is a library → SUMMARIZE into `wiki/`
  (update in place). `kdb/inbox/` is a mailroom → APPLY the wiki lens →
  `assessments/` (dated, append-only). Never summarize inbox material into wiki/.
- **Three clocks.** Arrival drives collection; validity drives tier routing,
  date-stamping, and retention; verdict drives feedback scoring. They are
  declared in domain_knowledge.md's temporal profile — derive, don't hard-code.
- **Data folders stay out of git.** `kdb/`, `wiki/`, `assessments/`, `.state/`
  contents are gitignored and backed up by `src/backup.py`.
- **Answer only from the knowledge base** when serving — the canon's boundary
  is the knowledge boundary; say "not covered" rather than improvising.
- **Update `progress.md`** at the end of every session and every run.
