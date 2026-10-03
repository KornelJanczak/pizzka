# Pizzka Backend

FastAPI service for the Pizzka application.

## Setup

From this directory, create and activate a virtual environment, then install the project with development dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

With `uv`, run the commands from `backend/` and use native system TLS certificates if PyPI certificate validation fails:

```bash
uv sync --native-tls --all-extras
uv run --native-tls fastapi dev
```

If another virtual environment is active, run `deactivate` first or use `uv run --active` after activating `backend/.venv`.

## Run

```bash
uvicorn app.main:app --reload
```

The API is available at `http://127.0.0.1:8000`. Interactive documentation is available at `/docs`.

## Test

```bash
pytest
```

There are currently no required environment variables.
