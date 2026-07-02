from fastapi import FastAPI

app = FastAPI(title="AI Workspace Backend")

@app.get("/health")
def health_check():
  return {"status": "ok", "service": "ai-workspace-backend"}
