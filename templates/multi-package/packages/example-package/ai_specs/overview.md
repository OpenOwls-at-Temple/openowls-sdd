# Overview — Package: example-package
> **OpenOwls SDD — Suite Edition.** Private to **this package**. Read by anyone consuming or building this library.
> Describes what *this one library* does, its public API, and who depends on it.
> For the whole-stack purpose, see the root `ai_specs/overview.md`; for the layering, see the root `ai_specs/architecture-planning.md`.

---

## Package Name
<!-- The real package name (rename from example-package). -->

_example-package_

## One-Line Description
<!-- What does this library do, in a single sentence? -->

_A [base/middle/top] library that [core responsibility]._

---

## Place in the Stack
<!-- Where this package sits and what it is allowed to depend on (downward only). -->

| Property | Value |
|----------|-------|
| Layer | _e.g. Base / Middle / Top_ |
| Depends on | _e.g. (nothing internal) / core / middleware_ |
| Consumed by | _e.g. middleware, app_ |

---

## Public API
<!-- The contract higher layers may use. Everything not listed here is internal and off-limits. -->

| Symbol | Kind | Description |
|--------|------|-------------|
| _e.g. `RecordStore`_ | _Class_ | _Primary entry point for storing records_ |
| _e.g. `compute_score()`_ | _Function_ | _Returns a score for a record_ |

> Anything not listed here is **internal** — other packages must not import it.

---

## Responsibilities
<!-- What this package is responsible for — and explicitly NOT responsible for. -->

**This package owns:**
- _e.g. Defining the Record data model_

**This package does NOT own:**
- _e.g. Orchestration (that's middleware) or user interaction (that's app)_

---

## Key Constraints
<!-- Limits specific to this library. -->

- _e.g. Must remain usable as a stand-alone library with no knowledge of higher layers_
