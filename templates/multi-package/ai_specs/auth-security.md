# Authentication & Security — Shared Policy
> **OpenOwls SDD — Suite Edition.** Shared, system-wide. Read by every engineer and the AI coding assistant.
> This file holds the **shared identity model and security posture** for the whole suite.
> **Caveat:** implementation specifics for a given boundary (e.g. the auth check in the top `app` layer) can move
> into the package that owns that boundary. Keep this file to policy that applies across packages.

---

## User Model & Scale (Shared)
<!-- Decide this before any auth code. It shapes architecture across the stack. -->

| Question | Decision |
|----------|----------|
| Expected number of users | _e.g. ~200 students; design for hundreds, not millions_ |
| User model | _e.g. Multi-user, single-tenant_ |
| Where auth is enforced | _e.g. At the top `app` layer; lower packages assume an already-authenticated caller_ |
| Anonymous / guest access? | _e.g. No — every action requires a logged-in account_ |

---

## Identity Strategy (Shared)
<!-- The biggest auth decision: build identity yourself or delegate it? -->

| Setting | Decision |
|---------|----------|
| Approach | _e.g. Third-party OAuth / email+password / managed service_ |
| Why this approach | _e.g. "Sign in with Google" avoids storing passwords_ |
| Identity provider(s) | _e.g. Google Workspace SSO for @temple.edu accounts_ |

---

## Authorization & Roles (Shared)
<!-- What an authenticated user may do. Enforce at the boundary; lower layers trust the caller. -->

| Role | Permissions |
|------|-------------|
| _e.g. User_ | _Can act on their own records only_ |
| _e.g. Admin_ | _Can manage all users and content_ |

- **Enforcement point:** _e.g. The `app` layer checks authorization on every protected entry point; `core`/`middleware` operate on already-authorized data._
- **Default posture:** _e.g. Deny by default — private unless explicitly marked public._

---

## Secrets Management (Shared)
<!-- How secrets are handled across the monorepo. -->

- All secrets live in environment variables, never in committed code.
- For a stack sharing one LLM provider key, a **single root `.env`** is usually simpler than one per package; `.env` is git-ignored and a `.env.example` with dummy values is checked in.
- Each environment (local, staging, production) uses separate secrets.
- Rotate any secret immediately if it is accidentally committed.

---

## Sensitive Data (Shared)
<!-- What is sensitive and how each kind is protected, suite-wide. -->

| Data | Classification | Protection |
|------|---------------|------------|
| _e.g. Passwords_ | _Secret_ | _Hashed, never logged, never returned_ |
| _e.g. API keys_ | _Secret_ | _Environment variables only_ |
| _e.g. PII_ | _PII_ | _Access-controlled; never sent to the LLM_ |

---

## Common Threats & Mitigations (Shared)
<!-- How the suite defends against the most common attacks. -->

| Threat | Mitigation |
|--------|------------|
| Injection (SQL / command) | _e.g. Parameterized queries / no string-built commands_ |
| Broken access control | _e.g. Re-check ownership at the boundary on every access_ |
| Sensitive data exposure | _e.g. HTTPS everywhere; never return secrets in responses_ |
| Cross-layer trust mistakes | _e.g. Don't let a lower package skip validation assuming the caller checked_ |

---

## Security Checklist Before Deploy
<!-- A quick pass before shipping any package. -->

- [ ] No secrets in the repository or in any package
- [ ] Auth/authorization enforced at the boundary, server-side
- [ ] Input validated where it enters the system
- [ ] Dependencies checked for known vulnerabilities
- [ ] No PII sent to the LLM

---

## What Claude Code Should Never Do

- Never store secrets, tokens, or passwords in committed code
- Never disable authentication or authorization checks "temporarily"
- Never log passwords, tokens, or PII
- Never trust input crossing a package boundary without validation
