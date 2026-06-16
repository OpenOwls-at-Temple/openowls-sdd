# Overview — The Suite
> **OpenOwls SDD — Suite Edition.** Shared, system-wide. Read by the business sponsor and the full team.
> Describes the **whole stack** at a high level: what it is, why it exists, who it is for, and the packages it is composed of.
> Each package also has its *own* `ai_specs/overview.md` describing that one library — this file is the system scope; those are the package scope.

---

## Suite Name
<!-- The name of the overall product / library suite -->

_Suite Name Here_

## One-Line Description
<!-- Summarize the whole stack in a single sentence -->

_A suite of [type] libraries that together [core value the stack delivers]._

---

## Problem Statement
<!-- What problem does this suite solve? Why does it need to exist as a stack of libraries rather than one app? -->

_Describe the problem here, and why the work is split across stacked packages._

---

## Goals
<!-- What does success look like for the whole stack? List 3-5 measurable goals. -->

- Goal 1
- Goal 2
- Goal 3

## Non-Goals
<!-- What is explicitly out of scope for the suite as a whole? -->

- Non-goal 1
- Non-goal 2

---

## The Packages
<!-- List every package in the suite, bottom-up (foundation first).
     "Depends On" must point downward only — never to a package above it. -->

| Order | Package | Layer | Responsibility | Depends On |
|-------|---------|-------|----------------|------------|
| 1 | _e.g. core_ | Base | _Foundational types, models, and pure logic_ | _(nothing internal)_ |
| 2 | _e.g. middleware_ | Middle | _Orchestration built on `core`'s public API_ | _core_ |
| 3 | _e.g. app_ | Top | _User- and model-facing layer_ | _middleware_ |

> The authoritative layering and dependency rules live in `ai_specs/architecture-planning.md`.

---

## Target Users / Consumers
<!-- Who uses the suite? Distinguish end users of the top layer from developers who consume lower packages. -->

| Audience | Description |
|----------|-------------|
| End users | _e.g. People interacting with the top `app` layer_ |
| Internal consumers | _e.g. Higher packages that import a lower package's public API_ |

---

## Shared Tech Stack
<!-- Technologies common to the whole suite. Package-specific choices go in that package's specs. -->

| Layer | Technology | Notes |
|-------|------------|-------|
| Language | _e.g. Python 3.11+_ | One version across all packages |
| Packaging | _e.g. one `.venv` + `requirements.txt` per package_ | Never cross-activated |
| AI / LLM | _e.g. Claude claude-sonnet-4-6 via Anthropic API_ | Shared model choice (see `llm-integration.md`) |
| Tooling | _e.g. black, pytest_ | Shared standard (see `conventions.md`) |

---

## Stakeholders
<!-- Who is involved and in what capacity? -->

| Name / Role | Responsibility |
|-------------|----------------|
| Faculty Sponsor | Defines scope, reviews milestones |
| Student Team | Design, implementation, deployment of each package |
| End Users | Testing and feedback |

---

## Key Constraints
<!-- Time, budget, technical, or compliance limits that apply across the suite. -->

- _e.g. Must be completed within one semester_
- _e.g. Lower packages must stay usable as stand-alone libraries_
