# Design — Shared

> **OpenOwls SDD — Suite Edition.** Shared, system-wide. Read by every engineer and the AI coding assistant.
> Captures the system architect's design instructions and specifications that apply across the **whole suite**.
> This is the "how it should be designed" companion to `architecture-planning.md` (which owns THE layering and dependency direction). Package-specific internal design lives in each package's `ai_specs/architecture.md`.

---

## Design Overview
<!-- One or two sentences describing the overall design intent for the suite. -->

_e.g. Each package exposes a small, stable public API and hides its internals, so higher layers depend on contracts, not implementations._

---

## Design Principles (Shared)
<!-- Guiding principles every package should respect. -->

- _e.g. Depend on public APIs, never on internals_
- _e.g. A lower layer never assumes how a higher layer uses it_
- _e.g. Prefer explicit interfaces over shared mutable state_

---

## Design Instructions & Directives (Shared)
<!-- Specific, non-negotiable design instructions from the system architect. -->

| Directive | Applies To | Rationale |
|-----------|-----------|-----------|
| _e.g. Shared data models are defined once in the base package_ | _All packages_ | _Avoids duplicate, drifting definitions_ |
| _Add more_ | | |

---

## Cross-Package Design Specifications
<!-- Design specs that span more than one package (e.g. shared contracts, interfaces). -->

### [Contract / Interface Name]
- **Defined in:** _which package owns it_
- **Consumed by:** _which packages depend on it_
- **Contract:** _inputs, outputs, and expected behavior_
- **Stability:** _e.g. A breaking change requires a MAJOR version bump_

---

## Design Patterns (Shared)
<!-- Patterns to use across the suite, and anti-patterns to avoid. -->

| Use | Avoid |
|-----|-------|
| _e.g. Facade re-exported from each package's `__init__.py`_ | _e.g. Importing another package's `_internal`_ |

---

## Non-Functional Requirements (Shared)
<!-- Quality attributes the whole suite must satisfy. -->

| Attribute | Requirement |
|-----------|-------------|
| Performance | _e.g. A full-stack call completes in under N seconds_ |
| Scalability | _e.g. Lower packages stay usable as stand-alone libraries_ |
| Maintainability | _e.g. A package can be rebuilt without touching the layers above it_ |

---

## Design Constraints (Shared)
<!-- Limits the whole suite must work within. -->

- _e.g. Every package must remain independently installable_
- _e.g. No circular dependencies, ever_

---

## Open Design Questions
<!-- Cross-package design decisions not yet settled. -->

| Question | Affects | Status | Owner |
|----------|---------|--------|-------|
| _e.g. Where should shared validation live?_ | _core, middleware_ | _Open_ | _Student B_ |

---

## Design Review Criteria
<!-- A quick checklist to judge whether an implementation matches the intended design. -->

- [ ] Respects the downward-only dependency direction
- [ ] Uses only public APIs across package boundaries
- [ ] Follows the shared principles and directives above
- [ ] Meets the shared non-functional requirements
