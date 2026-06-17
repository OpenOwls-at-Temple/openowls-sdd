# Deployment — Package: package1
> **OpenOwls SDD — Suite Edition.** Private to **this package**. Read by engineers packaging this library.
> Defines how *this library* is built, versioned, and consumed by higher layers.
> Suite-wide deployment and shared environment variables live in the root specs; this file is package-specific.

---

## Packaging
<!-- How is this library built and made importable by higher layers? -->

| Setting | Value |
|---------|-------|
| Build tool | _e.g. setuptools / hatch / poetry_ |
| Import name | _e.g. `package1`_ |
| Distribution | _e.g. Installed editable into higher packages' venvs during development_ |

---

## Versioning
<!-- How does this library signal changes to the packages that depend on it? -->

| Setting | Value |
|---------|-------|
| Scheme | _e.g. SemVer (MAJOR.MINOR.PATCH)_ |
| Current version | _e.g. 0.1.0_ |
| Breaking-change policy | _e.g. A public API change bumps MAJOR and is announced in `project_progress.md`_ |

---

## Environment
<!-- This package's OWN environment. One venv per package, never cross-activated. -->

- Environment: **`./.venv`** (git-ignored)
- Dependencies: **`./requirements.txt`** only
- Setup:

```bash
cd package1
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

---

## Environment Variables (Package-Specific)
<!-- Only variables THIS package needs. Shared ones (e.g. ANTHROPIC_API_KEY) live in the root specs / root .env.
     Never put actual values here. -->

| Variable | Required | Description |
|----------|----------|-------------|
| _`VARIABLE_NAME`_ | _Yes/No_ | _Description_ |

> A stack sharing one LLM provider key is usually simplest with a single root `.env`. See the root `auth-security.md`.

---

## How Higher Layers Consume This Package
<!-- The integration contract for packages above this one. -->

- Higher layers import only this package's **public API** (see `architecture.md`).
- _e.g. Add `package1` to the higher package's `requirements.txt` (editable/local path during development)._

---

## Build & Test Before Higher Layers Depend on It
<!-- A lower package must be solid before anything builds on it. -->

- [ ] This package's tests pass inside its own venv
- [ ] Public API is settled (no churn expected this phase)
- [ ] Version recorded and the root `project_progress.md` rollup updated

---

## Common Issues
<!-- Problems encountered and how to fix them. -->

| Issue | Likely Cause | Fix |
|-------|-------------|-----|
| Import fails in a higher package | Package not installed in that package's venv | Install it into the consuming package's `./.venv` |
| _Add more as you encounter them_ | | |
