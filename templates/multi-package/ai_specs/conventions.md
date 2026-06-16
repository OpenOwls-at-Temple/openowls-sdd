# Conventions — Shared
> **OpenOwls SDD — Suite Edition.** Shared, system-wide. Read by every engineer and the AI coding assistant.
> **One** standard for **all** packages. Copying these rules into a package guarantees drift the moment a rule changes,
> so this file lives once at the root and is inherited everywhere. Claude Code must follow it without being reminded.

---

## Language & Framework Versions
<!-- One version per technology, across the whole suite. -->

| Technology | Version |
|------------|---------|
| Python | 3.11+ |
| _Add more_ | |

---

## Naming Conventions

| Context | Convention | Example |
|---------|------------|---------|
| Python variables & functions | `snake_case` | `compute_score()` |
| Python classes | `PascalCase` | `RecordStore` |
| Modules / files | `snake_case` | `record_store.py` |
| Packages (directories) | `snake_case`, short | `core`, `middleware`, `app` |
| Environment variables | `UPPER_SNAKE_CASE` | `ANTHROPIC_API_KEY` |
| Git branches | `type/short-description` | `feature/core-record-model` |

---

## Monorepo Rules
<!-- Conventions specific to a stacked, multi-package suite. -->

- Dependencies point **downward only**. A higher layer may import a lower one through its **public API**; a lower layer must never depend on a higher one.
- Never reach around a package's public API into its internals — treat each package like a third-party library.
- Each package has its **own** `./.venv` and `./requirements.txt`. Activate only the current package's venv; never cross-activate a sibling's.
- Shared specs live **once** at the root. Never copy a root spec into a package.
- Log work in **two** places: the package's `progress.md` and the root `project_progress.md`.

---

## Code Style

- **Python:** Follow PEP 8. Use `black` for formatting.
- Maximum line length: 100 characters
- No commented-out code in commits — delete it or add a `TODO:` with explanation
- Public APIs are documented with docstrings; internal helpers are clearly marked private

---

## Git Conventions

- Commit messages follow `type: short description`
  - Types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`
  - When a change is scoped to one package, name it: `feat(core): add record model`
- Every feature on its own branch; no direct commits to `main`
- Pull requests require at least one review before merging

---

## Testing Conventions

- Every package has its **own** test suite that runs inside its own venv
- A lower package's tests must pass before a higher package builds on it
- Test file naming: `test_[module_name].py`
- Use descriptive test names: `test_record_is_immutable_after_publish`

---

## LLM / AI Conventions
<!-- How the team uses AI assistants and how LLM calls are written. Shared policy lives in `llm-integration.md`. -->

- All prompts live in the package that owns the LLM call — never hardcoded inline in unrelated modules
- All LLM calls must have error handling and a fallback response
- Do not send personally identifiable information (PII) to the LLM

---

## What Claude Code Should Never Do

- Never modify files in any `ai_specs/` folder without explicit instruction
- Never cross the dependency direction (no lower layer depending on a higher one)
- Never activate or install into a sibling package's environment
- Never skip writing tests to save time
- Never use a library not in the relevant package's `requirements.txt` without asking first
