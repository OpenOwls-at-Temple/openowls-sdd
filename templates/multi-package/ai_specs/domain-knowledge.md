# Domain Knowledge — Shared
> **OpenOwls SDD — Suite Edition.** Shared, system-wide. Read primarily by the AI coding assistant.
> Captures domain concepts, terminology, business rules, and constraints that apply across the **whole suite**.
> Define shared vocabulary here once so every package uses the same terms. Faculty seeds this file; students expand it.

---

## Domain Overview
<!-- What domain does this suite operate in? Give a brief description. -->

_e.g. This suite operates in the [domain], split into a foundational data/logic layer, an orchestration layer, and a user-facing layer._

---

## Key Concepts & Terminology
<!-- Define terms with a specific meaning in this domain. Shared across all packages
     so the AI never assigns different meanings in different layers. -->

| Term | Definition | Primarily used in |
|------|------------|-------------------|
| _e.g. Record_ | _A single unit of domain data_ | _core_ |
| _e.g. Pipeline_ | _An ordered sequence of orchestration steps_ | _middleware_ |
| _Add more_ | | |

---

## Business Rules
<!-- Rules that must always hold, regardless of which package implements them. -->

- _e.g. A Record is immutable once published_
- _e.g. All timestamps are stored in UTC_

---

## Domain Constraints
<!-- Technical or domain limitations every package should respect. -->

- _e.g. The LLM should never receive more than N records at once to avoid token limits_
- _e.g. Identifiers are globally unique across the suite_

---

## Common Pitfalls
<!-- Things that are easy to get wrong in this domain or across layers. -->

- _e.g. Don't redefine a shared term differently in a higher layer_
- _e.g. Don't let `core` make assumptions about how `app` presents data_

---

## External Dependencies & Integrations
<!-- Third-party services, APIs, or data sources the suite depends on. -->

| Service | Purpose | Used by | Notes |
|---------|---------|---------|-------|
| _e.g. Anthropic API_ | _LLM calls_ | _e.g. app_ | _Rate limits apply_ |
| _Add more_ | | | |

---

## References
<!-- Links to external documentation, papers, or resources relevant to this domain. -->

- _e.g. [Anthropic API Docs](https://docs.anthropic.com)_
