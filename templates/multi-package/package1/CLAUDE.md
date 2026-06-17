# CLAUDE.md — Package: package1
> **OpenOwls SDD — Suite Edition.** This is **one package** inside the suite.
> Rename `package1` to your real package name and copy this whole folder shape for every package.
> This file loads **on demand** — the first time Claude Code reads a file in this package — and it *inherits* the
> root `CLAUDE.md` and all shared `ai_specs/` automatically (Claude Code walks up the directory tree).

## Read These First (This Package)

1. **`./progress.md`** — this package's session memory
2. **`./ai_specs/overview.md`** — what this library does, its public API, and who consumes it
3. **`./ai_specs/features.md`** — this library's capabilities, phased
4. **`./ai_specs/architecture.md`** — this library's internal design
5. **`./ai_specs/deployment.md`** — how this library is packaged and versioned

You also inherit, from the suite root: `overview.md`, `architecture-planning.md` (the layering), `domain-knowledge.md`, `llm-integration.md`, `conventions.md`, and `auth-security.md`. Follow them without restating them here.

## Environment Rules (This Package Only)

- Before running, testing, or installing anything: activate **`./.venv`**.
- Install dependencies only from **`./requirements.txt`** into that venv.
- **Never** activate or modify a sibling package's environment.

## Layer Discipline

- This package's place in the stack and its dependencies are defined in the root `ai_specs/architecture-planning.md`.
- Depend **downward only**, through a lower package's **public API** — never reach into its internals.
- Never let this package depend on a package above it.

## Before You Finish a Session

- Update **`./progress.md`** for this package.
- Update the root **`project_progress.md`** rollup so the whole-stack view stays current.
