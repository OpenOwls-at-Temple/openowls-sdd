# Architecture Planning — The Layering
> **OpenOwls SDD — Suite Edition.** Shared, system-wide. Read by the system architect and every engineer.
> This file owns **THE layering**: which packages exist, what order they stack in, and which direction dependencies flow.
> This is inherently *between* packages, so it cannot live inside any single one. Each package's *internal* design lives in its own `ai_specs/architecture.md`.

---

## System Architecture Overview
<!-- Describe the stack at a high level. How do the packages compose into a working whole? -->

_e.g. A stack of Python libraries. `core` holds foundational logic, `middleware` orchestrates it, and `app` is the user- and model-facing layer. Each is an independently installable package; higher layers import lower ones through their public API only._

---

## The Layers (Bottom-Up)
<!-- List every package, foundation first. "Depends On" must point downward only. -->

| Order | Package | Layer | Responsibility | Depends On |
|-------|---------|-------|----------------|------------|
| 1 | _e.g. core_ | Base | _Foundational types, models, pure logic_ | _(nothing internal)_ |
| 2 | _e.g. middleware_ | Middle | _Orchestration on top of `core`_ | _core_ |
| 3 | _e.g. app_ | Top | _User- and model-facing layer_ | _middleware_ |

---

## Dependency Direction — Downward Only
<!-- The single most important rule of the suite. -->

- A higher layer **may** depend on a lower one, and only through its **public API**.
- A lower layer **must never** import or depend on a higher one.
- No circular dependencies. If two packages need each other, something belongs in a shared lower layer.
- Reaching around a package's public API into its internals is forbidden — treat each package like a third-party library.

```
app          (Layer 3 · Top)
  ↓ depends on
middleware   (Layer 2 · Middle)
  ↓ depends on
core         (Layer 1 · Base)
```

---

## Public API Boundaries
<!-- For each package, what is the contract that higher layers are allowed to use? -->

| Package | Public API surface | What is internal (off-limits) |
|---------|--------------------|-------------------------------|
| _e.g. core_ | _e.g. `core.models`, `core.compute()`_ | _e.g. `core._internal`, private helpers_ |
| _e.g. middleware_ | _e.g. `middleware.Orchestrator`_ | _e.g. internal adapters_ |

---

## Repository Layout (Monorepo)
<!-- The two-tier structure. Operational files sit loose; specs live in ai_specs/. -->

```
your-suite/
├── CLAUDE.md                 # system entry point (loose)
├── project_progress.md       # stack-wide rollup (loose)
├── ai_specs/                 # SHARED, system-wide specs
│   ├── overview.md
│   ├── domain-knowledge.md
│   ├── conventions.md
│   ├── llm-integration.md
│   ├── auth-security.md
│   └── architecture-planning.md
├── package1/                 # one package — repeat this shape per package (rename to your real package)
│   ├── CLAUDE.md             # package entry (loose)
│   ├── progress.md           # package session memory (loose)
│   ├── ai_specs/             # PRIVATE, per-package specs
│   │   ├── overview.md
│   │   ├── features.md
│   │   ├── architecture.md
│   │   └── deployment.md
│   ├── .venv/                # package-owned environment (git-ignored)
│   └── requirements.txt
└── package2/                 # another package, same shape (add one folder per package)
```

---

## Build & Integration Order
<!-- In a stacked suite, dependency order IS a phasing discipline. -->

1. Build and stabilize the **base package** first — tests pass and its public API is settled before anything depends on it.
2. Build each higher layer only once the layer below is stable.
3. Integrate upward through public APIs; never reach into internals.

---

## Per-Package Environment Convention
<!-- One environment per package. This prevents "works on my machine" bugs across layers. -->

- Every package has its **own** `./.venv` and `./requirements.txt`.
- Activate only the current package's venv; install only from its `requirements.txt`.
- **Never** activate or modify a sibling package's environment.
- `.venv/` is git-ignored in every package.

---

## Shared Environment Variables
<!-- Variables common to the whole suite. Package-specific vars go in that package's deployment.md.
     Never put actual values here. -->

| Variable | Description |
|----------|-------------|
| `ANTHROPIC_API_KEY` | Anthropic API key for LLM calls (shared across the suite) |
| _`VARIABLE_NAME`_ | _Description_ |

> A stack that shares one LLM provider key is usually simplest with a **single root `.env`**. See `auth-security.md` and each package's `deployment.md`.

---

## Cross-Package Design Decisions
<!-- Architectural choices that affect more than one package. -->

| Decision | Choice | Reason |
|----------|--------|--------|
| _e.g. Inter-package communication_ | _Direct import of public API_ | _Simplest for a single monorepo_ |
| _e.g. Shared data models_ | _Defined once in `core`_ | _Avoids duplicate, drifting definitions_ |
