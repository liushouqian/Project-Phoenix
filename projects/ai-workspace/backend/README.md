# AI Workspace Backend

## Goal

Backend service for AI Workspace.

## Tech Stack

- Python
- FastAPI


## Run locally

```bash
cd projects/ai-workspace/backend
source .venv/bin/activate
python -m uvicorn main:app --reload

## Current Status

- [⎷] FastAPI project initialized
- [⎷] Health check endpoint added
- [⎷] Chat API skeleton added
- [ ] LLM integration
- [ ] Tool calling
- [x] Task 5 — Add session-based in-memory conversation history to `/chat`
- Verified that the same session can remember user profile information across multiple turns.

## Current Progress Note

- 全面更改模型为DeepSeek

## Run the backend

```bash
python -m uvicorn main:app --reload