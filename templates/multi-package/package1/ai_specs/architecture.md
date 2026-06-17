# Architecture — Package: package1
> **OpenOwls SDD — Suite Edition.** Private to **this package**. Read by engineers working inside this library.
> Defines this library's **internal** design — its modules, key types, and data flow.
> This is the *within*-package design. The *between*-package layering lives in the root `ai_specs/architecture-planning.md`.

---

## Internal Overview
<!-- How is this package organized internally? How does data flow through it? -->

_e.g. A small set of modules: a data model, a store that persists it, and a public facade that higher layers import._

---

## Internal Folder Structure
<!-- The source layout INSIDE this package. -->

```
package1/
├── src/
│   └── package1/
│       ├── __init__.py        # Public API surface (what higher layers import)
│       ├── models.py          # Internal data models
│       ├── service.py         # Core logic
│       └── _internal/         # Private helpers — never imported by other packages
├── tests/                     # This package's own test suite
├── ai_specs/
├── CLAUDE.md
├── progress.md
└── requirements.txt
```

---

## Public API vs. Internal
<!-- Restate the boundary so it's enforced during implementation. -->

- **Public (importable by higher layers):** _e.g. everything re-exported from `__init__.py`_
- **Internal (off-limits to other packages):** _e.g. `_internal/`, private functions, anything not re-exported_

---

## Key Types & Modules
<!-- The main internal building blocks. -->

| Module / Type | Responsibility |
|---------------|----------------|
| _e.g. `models.Record`_ | _The core data entity_ |
| _e.g. `service.RecordStore`_ | _Stores and retrieves records_ |

---

## Dependencies on Lower Packages
<!-- Which lower packages this one uses, and through which public API. Downward only. -->

| Lower Package | Public API used | Why |
|---------------|-----------------|-----|
| _(nothing internal)_ | — | _e.g. This is the base layer_ |

---

## Internal Design Decisions
<!-- Choices that matter inside this package. -->

| Decision | Choice | Reason |
|----------|--------|--------|
| _e.g. Persistence_ | _In-memory for Phase 1_ | _Keeps the base layer simple; swap later_ |

---

## LLM Usage (If Any)
<!-- Only if THIS package calls the model. Follow the shared guardrails in the root `llm-integration.md`. -->

- **Does this package call the LLM?** _e.g. No — pure logic, no model calls_
- If yes: keep all prompt templates here, follow the root `llm-integration.md` policy, and document the context strategy and fallbacks.
