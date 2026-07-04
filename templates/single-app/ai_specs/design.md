# Design

> **OpenOwls SDD** — Read by engineers and the AI coding assistant.
> Captures the system architect's design instructions and specifications — the principles, directives, and standards engineers (and Claude Code) must follow when building.
> This is the "how it should be designed" companion to `architecture-planning.md` (which owns structure, data models, and APIs). Keep design intent here; keep concrete structure there.

---

## Design Overview
<!-- One or two sentences describing the overall design intent and philosophy. -->

_e.g. The system favors small, single-responsibility modules with explicit interfaces, so features can be added without rewriting existing code._

---

## Design Principles
<!-- The guiding principles every design decision should respect. -->

- _e.g. Prefer composition over inheritance_
- _e.g. Fail loudly — surface errors early rather than swallowing them_
- _e.g. Keep the UI layer free of business logic_

---

## Design Instructions & Directives
<!-- Specific, non-negotiable instructions from the system architect. -->

| Directive | Rationale |
|-----------|-----------|
| _e.g. All external calls go through a single client wrapper_ | _Centralizes retries, logging, and error handling_ |
| _Add more_ | |

---

## Design Specifications
<!-- Detailed design specs for specific components, modules, or interfaces. -->

### [Component / Module Name]
- **Responsibility:** _What this piece is responsible for_
- **Interface / Contract:** _Inputs, outputs, and expected behavior_
- **Constraints:** _Any limits or rules it must obey_

---

## Design Patterns
<!-- Patterns to use, and anti-patterns to avoid. -->

| Use | Avoid |
|-----|-------|
| _e.g. Repository pattern for data access_ | _e.g. Direct SQL scattered across route handlers_ |

---

## Non-Functional Requirements
<!-- Quality attributes the design must satisfy. -->

| Attribute | Requirement |
|-----------|-------------|
| Performance | _e.g. A page loads in under 2 seconds on a typical connection_ |
| Scalability | _e.g. Handles hundreds of concurrent users without redesign_ |
| Maintainability | _e.g. A new student can add a feature without touching unrelated modules_ |
| Accessibility | _e.g. Meets basic WCAG AA contrast and keyboard navigation_ |

---

## UI / UX Design Guidelines
<!-- Only if the project has a user interface. Visual and interaction standards. -->

- _e.g. Use the shared component library for all form controls_
- _e.g. Every destructive action requires a confirmation step_

---

## Design Constraints
<!-- Limits the design must work within — technical, budget, or platform. -->

- _e.g. Must run within free-tier hosting limits_
- _e.g. No native mobile app — responsive web only_

---

## Open Design Questions
<!-- Design decisions not yet settled. Resolve these before building the affected part. -->

| Question | Status | Owner |
|----------|--------|-------|
| _e.g. Which state-management approach for the frontend?_ | _Open_ | _Student B_ |

---

## Design Review Criteria
<!-- A quick checklist to judge whether an implementation matches the intended design. -->

- [ ] Follows the design principles above
- [ ] Respects all directives in this file
- [ ] Meets the non-functional requirements
- [ ] No forbidden anti-patterns introduced
