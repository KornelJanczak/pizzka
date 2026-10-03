---
name: FastAPI Python backend
description: "Use when creating or changing the FastAPI Python service under backend/."
applyTo: "backend/**/*.py,backend/**/*.toml,backend/**/*.yaml,backend/**/*.yml,backend/**/*.json"
---

# FastAPI Backend

- Keep the ASGI application entry point discoverable, preferably as `backend/app/main.py` with an `app` object.
- Organize non-trivial endpoints into routers and keep request/response contracts in Pydantic schemas rather than assembling unvalidated dictionaries in route handlers.
- Keep settings, persistence, and external-service access behind small modules so route handlers remain easy to test.
- Use async handlers only when their dependencies are async; do not block the event loop with synchronous I/O in async routes.
- Validate inputs at the boundary, return explicit response models and status codes, and avoid leaking internal exception details.
- Add tests for success, validation failure, and relevant error paths. Prefer isolated test fixtures and avoid requiring live external services.
- Document Python version, dependency installation, server startup, test commands, and required environment variables in backend documentation when those conventions are introduced.
- Run formatting, linting, type checking, and `pytest` for the backend checks that are configured. Report unavailable tools instead of silently skipping them.
