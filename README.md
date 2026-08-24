# ai-architect-knowledge-assistant
AI Architect Knowledge Assistant

## Setup and Run

From the repository root, create and activate a Python environment with `uv`:

```bash
python -m pip install uv
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

Run the application:

```bash
uvicorn backend.app.main:app --reload
```

The API provides `GET /health`, `GET /projects`, and `POST /project`.
