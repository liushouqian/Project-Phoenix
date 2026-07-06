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

## Current Progress Note

- `/health` 已跑通
- `/chat` 已成功接入真实 LLM
- 使用 OpenRouter 时，`openrouter/free` 返回表现异常，改为具体免费模型后恢复正常
- 当前可用模型：
  - `meta-llama/llama-3.3-8b-instruct:free`
- Day 3 尚未正式收尾，README / journal / 收尾补丁待后续完成