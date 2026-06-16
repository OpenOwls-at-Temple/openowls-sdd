# LLM Integration — Shared Policy
> **OpenOwls SDD — Suite Edition.** Shared, system-wide. Read by engineers and faculty.
> This file holds the **shared LLM policy** for the whole suite: model choice and guardrails.
> **Caveat:** if only one package (typically the top `app`) actually calls the model, the per-feature prompt
> templates, context strategy, and call flow belong in **that package's** `ai_specs/`. Keep this file to policy.

---

## Which Packages Use the LLM
<!-- Be explicit. In a stack, the model is often called from only the top layer. -->

| Package | Calls the LLM? | What for |
|---------|----------------|----------|
| _e.g. core_ | No | _Pure logic; no model calls_ |
| _e.g. middleware_ | No | _Orchestration only_ |
| _e.g. app_ | Yes | _User-facing generation / reasoning_ |

> If exactly one package calls the model, move the prompt specifics into that package's specs and keep only the shared policy below.

---

## Model (Shared Choice)

| Setting | Value |
|---------|-------|
| Provider | _e.g. Anthropic_ |
| Model | _e.g. claude-sonnet-4-6_ |
| Why this model | _e.g. Best balance of reasoning quality and cost for our use case_ |
| API key location | _e.g. Shared root `.env` → `ANTHROPIC_API_KEY`, read server-side only_ |

---

## Guardrails (Shared)
<!-- Rules every LLM call in the suite must obey, wherever it lives. -->

- **Never** send PII or secrets to the model.
- Every call has error handling and a fallback response.
- Validate and parse model output before trusting it; never execute raw output.
- Cap input size to stay within context limits (define the cap per feature in the owning package).
- Log enough to debug failures, but never log prompts that contain user data.

---

## Where Prompts Live
<!-- Pointer, not the prompts themselves. -->

- Prompt templates and the per-feature context strategy live in the owning package's `ai_specs/` (e.g. `packages/app/ai_specs/architecture.md` or a dedicated prompts section).
- Keep all prompts for a package in one place within that package — never scattered inline.

---

## Cost & Context (Shared Expectations)
<!-- Set suite-wide expectations; exact numbers per feature live with the package. -->

| Concern | Shared expectation |
|---------|--------------------|
| Cost awareness | _e.g. Each feature documents its estimated tokens and cost per call_ |
| Context limits | _e.g. No call exceeds the model's context window; large inputs are summarized or chunked_ |
| Data retention | _e.g. Verify the provider's current API data-retention policy_ |

---

## Evaluation (Shared Bar)
<!-- What "good" means for any LLM feature in the suite. Per-feature metrics live with the package. -->

| Metric | How to Measure | Target |
|--------|---------------|--------|
| _e.g. Output validity_ | _Parse-success rate logged in the calling package_ | _>98%_ |
| _e.g. Fallback rate_ | _Logged when a fallback is returned_ | _<2%_ |
