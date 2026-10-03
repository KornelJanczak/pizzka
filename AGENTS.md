# Repository Instructions

## Repository Layout

- `frontend/` is a Next.js App Router application. Keep page and layout boundaries in `frontend/app/` and static assets in `frontend/public/`.
- `backend/` is reserved for the FastAPI Python service. Establish backend conventions there before adding API code; do not place Python files in the repository root.
- Keep frontend and backend commands scoped to their own directories until a root-level task runner is intentionally added.

## Working Conventions

- Inspect nearby implementations and existing documentation before introducing abstractions.
- Keep API routes, schemas, settings, and infrastructure concerns separated as the backend grows.
- Load configuration from environment variables or a settings module; never commit secrets or local `.env` files.
- Preserve strict TypeScript settings and the existing Next.js/Tailwind setup unless the task requires a deliberate change.
- Add focused tests for new backend behavior and update documentation when commands, endpoints, or environment variables change.

## Validation

From `frontend/`, run `npm run lint`, `npm run build`, and `npx tsc --noEmit` when frontend files change. For backend changes, use the project's Python environment and run the configured formatter, type checker, and `pytest` suite; if those tools do not yet exist, document the chosen commands in the change.

## Branch Push Report

Before recommending a push, report the current branch and base branch, summarize changed files and API behavior, list required setup and environment variables, record validation commands and results, and confirm that secrets and generated artifacts are excluded. Do not claim a check passed unless it was run successfully.

See [frontend/README.md](frontend/README.md) for the existing frontend setup details.
