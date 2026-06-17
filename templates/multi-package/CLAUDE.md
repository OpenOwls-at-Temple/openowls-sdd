# CLAUDE.md — Suite Root
> This is a **multi-package monorepo** built with the **OpenOwls SDD (Spec-Driven Development) Process — Suite Edition**.
> This file is the **system entry point**. Claude Code reads it — and every other `CLAUDE.md` on the path — by walking *up* the directory tree, so the shared specs below are inherited in **every** package.

## Session Startup — Read These First (Shared, System-Wide)

1. **`project_progress.md`** (root) — stack-wide status rollup and an index to each package's `progress.md`
2. **`ai_specs/overview.md`** — the whole stack's purpose, the packages, and who it is for
3. **`ai_specs/architecture-planning.md`** — THE layering: the packages, their order, and the dependency direction
4. **`ai_specs/domain-knowledge.md`** — shared terminology and business rules
5. **`ai_specs/llm-integration.md`** — shared model choice and guardrails
6. **`ai_specs/conventions.md`** — one shared coding / git / testing standard for every package
7. **`ai_specs/auth-security.md`** — shared identity model and security posture

When you start working inside a specific package, also read that package's `CLAUDE.md`, its `./ai_specs/`, and its `./progress.md`.

## How This Repo Is Structured (Two Tiers)

- **Tier 1 — Root (this folder):** shared specs every package inherits. Operational files (`CLAUDE.md`, `project_progress.md`) sit **loose** at the root; specs live inside `ai_specs/`.
- **Tier 2 — Each package (`<name>/` at the suite root):** its own `CLAUDE.md`, `progress.md`, `ai_specs/`, `.venv/`, and `requirements.txt`. Each package is a top-level folder; there is no wrapping `packages/` directory.

`CLAUDE.md` and the progress files are **operational** — they must sit at a folder root and *point into* `ai_specs/`. Never put them inside `ai_specs/`.

## Build Order — Bottom-Up

- Build and stabilize the **base package first**. Do not climb the stack until the layer below is solid.
- Dependencies point **downward only**. A higher layer may use a lower one through its **public API**; a lower layer must never depend on a higher one.
- See `ai_specs/architecture-planning.md` for the concrete package order.

## General Instructions

- Respect the downward-only dependency direction. Never reach around a package's public API into its internals.
- Each package owns its own environment. Activate only the current package's `./.venv` and install only from its `./requirements.txt`. **Never activate or modify a sibling package's environment.**
- After any meaningful unit of work, update **both** the package's `progress.md` and the root `project_progress.md`.
- Always work within the current phase of the package you are in. Do not implement future-phase features unless explicitly instructed.
- Never copy a root spec into a package — shared specs live **once**, at the root.
- If you encounter a conflict between specs (root or package), flag it to the user before proceeding.
- Never delete or overwrite any file in any `ai_specs/` folder without explicit instruction.
