# Features — Package: package1
> **OpenOwls SDD — Suite Edition.** Private to **this package**. Read by whoever defines and consumes this library.
> Defines what *this library* does, phased. Phase 1 is the smallest version that works end-to-end for this package.

---

## How to Read This File

- **Phase 1** — Must-have capabilities. The library is not usable by the next layer without these.
- **Phase 2** — Should-have capabilities. Added value once Phase 1 is stable.
- **Phase 3** — Nice-to-have / advanced capabilities.

> In a stacked suite, dependency order is itself a phasing discipline: this package's Phase 1 should be solid before a higher package builds on it.

---

## Phase 1 — Core Capabilities

### Capability 1: [Name]
**So that** [the consuming layer / user gets some value],
**this library can** [do something].

**Acceptance Criteria:**
- [ ] Given [context], when [the public API is called], then [outcome]
- [ ] Given [context], when [action], then [outcome]

---

### Capability 2: [Name]
**So that** [value],
**this library can** [do something].

**Acceptance Criteria:**
- [ ] Given [context], when [action], then [outcome]

---

## Phase 2 — Enhanced Capabilities

### Capability 3: [Name]
**So that** [value],
**this library can** [do something].

**Acceptance Criteria:**
- [ ] Given [context], when [action], then [outcome]

---

## Phase 3 — Advanced Capabilities

### Capability 4: [Name]
**So that** [value],
**this library can** [do something].

**Acceptance Criteria:**
- [ ] Given [context], when [action], then [outcome]

---

## Out of Scope
<!-- Capabilities that belong to a different layer or are explicitly excluded. -->

- _e.g. User-facing presentation (belongs in the top `app` package)_
- _e.g. Orchestration across packages (belongs in `middleware`)_
