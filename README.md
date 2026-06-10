# OpenOwls SDD

**A spec-driven development framework for student teams building real projects with AI coding assistants.**

OpenOwls SDD gives every project a shared language — a small set of specification files that keep students, faculty, and AI on the same page from day one. Instead of diving straight into code, teams spend a session writing specs first. The result: less confusion, better AI output, and a workflow that mirrors how professional software teams actually operate.

Inspired by the [GitHub Spec Kit](https://github.com/github/spec-kit), but deliberately simplified for a teaching context.

---

## The Key Differentiator — Stakeholder Framing

Most student projects have one role: "developer." OpenOwls SDD introduces a different mental model. Each spec file maps to a real professional role, so students learn to think from multiple perspectives before writing a single line of code.

| File | Professional Role It Mirrors |
|------|------------------------------|
| `overview.md` | Business sponsor defining the product vision |
| `features.md` | Product owner translating user needs into requirements |
| `architecture-planning.md` | System architect designing the technical approach |
| `domain-knowledge.md` | Domain expert briefing the engineering team |
| `conventions.md` | Engineering lead setting team standards |
| `llm-integration.md` | AI/ML engineer designing the intelligence layer |
| `deployment.md` | DevOps engineer owning the release pipeline |
| `progress.md` | Engineering team's daily standup and sprint tracker |

Every OpenOwls project includes an LLM layer — `llm-integration.md` is a first-class file, not optional.

---

## Folder Structure

Every OpenOwls SDD project follows this layout:

```
your-project/
├── CLAUDE.md                        ← tells Claude Code to read everything below in order
├── progress.md                      ← living session status, updated after every work session
└── ai_specs/
    ├── overview.md                  ← what the project is and why it exists
    ├── features.md                  ← what the app does, in plain language
    ├── architecture-planning.md     ← how it's built
    ├── domain-knowledge.md          ← concepts and constraints the team needs to understand
    ├── conventions.md               ← coding standards and workflow rules
    ├── deployment.md                ← how to ship it
    └── llm-integration.md           ← how AI fits into the product
```

The folder is always called `ai_specs/` — this is the OpenOwls convention.

---

## The Workflow

OpenOwls SDD uses a four-step process that splits planning from building:

**Step 1 — Draft specs with Claude.ai**
Start a conversation in [Claude.ai](https://claude.ai) and work through each spec file one at a time. Claude.ai is great for open-ended brainstorming and writing.

**Step 2 — Review with your team**
Read the specs as a group. Make sure everyone agrees on what you're building before any code is written. Faculty review `overview.md` and `features.md`; students own the rest.

**Step 3 — Fill in the gaps**
Complete any sections that need more detail. `architecture-planning.md`, `conventions.md`, and `llm-integration.md` often need a second pass once the team has talked things through.

**Step 4 — Build with Claude Code**
Open the project in [Claude Code](https://claude.ai/code). `CLAUDE.md` tells Claude Code to read all your specs before doing anything — so it starts with full context every session.

---

## Getting Started

Copy the `templates/` folder into your project root and start filling in the spec files.

Full walkthrough: [Getting Started Guide](docs/getting-started.html)

---

## This Repo

```
openowls-sdd/
├── templates/          ← copy these into your project
├── examples/
│   └── todo-app/       ← worked example (coming soon)
└── docs/
    └── getting-started.html
```

---

## Inspiration

OpenOwls SDD is inspired by the industry Spec-Driven Development movement:

- [GitHub Spec Kit](https://github.com/github/spec-kit)
- [GitHub Spec Kit Docs](https://github.github.com/spec-kit/)
- [Microsoft Developer Blog — Spec-Driven Development](https://developer.microsoft.com/blog/spec-driven-development-spec-kit)

OpenOwls SDD is its own framework — not a copy of any of the above. It is designed specifically for student teams who are learning to collaborate with AI tools on real projects.

---

[OpenOwls at Temple](https://openowls-at-temple.github.io/) · [GitHub Org](https://github.com/OpenOwls-at-Temple)
