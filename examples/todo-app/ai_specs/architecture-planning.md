# Architecture Planning

> **OpenOwls SDD** — Read by the system architect and software engineers.
> Defines the folder structure, key design decisions, and implementation details.
> Claude Code uses this file to understand how the codebase is organized.

---

## System Architecture Overview
<!-- Describe the high-level architecture. How do the main components interact? -->

_e.g. This is a three-tier web application: a React frontend, a FastAPI backend, and a PostgreSQL database. The backend exposes a REST API consumed by the frontend. An LLM layer is called server-side only._

---

## Folder Structure
<!-- Show the intended folder structure. Add a comment explaining each key folder. -->

```
project-root/
├── CLAUDE.md
├── progress.md
├── ai_specs/
├── frontend/
│   ├── src/
│   │   ├── components/     # Reusable UI components
│   │   ├── pages/          # Page-level components
│   │   ├── hooks/          # Custom React hooks
│   │   ├── services/       # API call functions
│   │   └── utils/          # Helper functions
│   └── public/
├── backend/
│   ├── app/
│   │   ├── routes/         # API route handlers
│   │   ├── models/         # Database models
│   │   ├── schemas/        # Pydantic request/response schemas
│   │   ├── services/       # Business logic
│   │   └── llm/            # LLM integration layer
│   └── tests/
└── docs/                   # Any additional documentation
```

---

## Key Design Decisions
<!-- Document important architectural choices and the reasoning behind them. -->

| Decision | Choice | Reason |
|----------|--------|--------|
| _e.g. API style_ | _REST_ | _Simpler for students to learn and debug_ |
| _e.g. Auth method_ | _JWT tokens_ | _Stateless, works well with React frontend_ |
| _e.g. LLM calls_ | _Server-side only_ | _Keeps API key secure, centralizes prompt logic_ |

---

## Data Models
<!-- Describe the main data entities and their key fields. -->

### [Entity Name]
| Field | Type | Description |
|-------|------|-------------|
| `id` | UUID | Primary key |
| `created_at` | DateTime | Record creation timestamp |
| _field_ | _type_ | _description_ |

---

## API Endpoints
<!-- List the main API endpoints. Add more as the project grows. -->

| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/[resource]` | _List all items_ |
| POST | `/api/[resource]` | _Create a new item_ |
| PUT | `/api/[resource]/:id` | _Update an item_ |
| DELETE | `/api/[resource]/:id` | _Delete an item_ |

---

## LLM Integration
<!-- If the project uses an LLM, describe how it is integrated. -->

- **Model:** _e.g. claude-sonnet-4-20250514_
- **Called from:** _e.g. backend service layer only_
- **Input:** _What context/data is passed to the LLM?_
- **Output:** _What does the LLM return?_
- **Prompt location:** _e.g. `/backend/app/llm/prompts.py`_

---

## Environment Variables
<!-- List all required environment variables. Never put actual values here. -->

| Variable | Description |
|----------|-------------|
| `ANTHROPIC_API_KEY` | Anthropic API key for LLM calls |
| `DATABASE_URL` | PostgreSQL connection string |
| _`VARIABLE_NAME`_ | _Description_ |

---

## Deployment
<!-- Deployment details are covered in `ai_specs/deployment.md` -->
