from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.schemas.chat import (
  ChatRequest,
  ChatResponse,
  ResetSessionRequest,
  ResetSessionResponse,
  HistoryRequest,
  HistoryResponse,
  ErrorResponse,
)
from app.services.chat_service import generate_reply
from app.services.conversation_store import (
  clear_history,
  get_history,
)
from app.core.exceptions import LLMServiceError

router = APIRouter()


@router.post(
  "/chat",
  response_model=ChatResponse,
  responses={
    500: {
      "model": ErrorResponse
    }
  }
)
def chat(request: ChatRequest):
  try:
    reply = generate_reply(
      session_id=request.session_id,
      message=request.message,
      metadata=request.metadata
    )
    return ChatResponse(reply=reply)
  except LLMServiceError:
    return JSONResponse(
      status_code=500,
      content={"error": "LLM request failed"}
    )

@router.post("/chat/reset", response_model=ResetSessionResponse)
def reset_chat(request: ResetSessionRequest):
  clear_history(request.session_id)
  return ResetSessionResponse(message="Session history cleared.")

@router.post("/chat/history", response_model=HistoryResponse)
def get_chat_history(request: HistoryRequest):
  history = get_history(request.session_id)
  return HistoryResponse(
    session_id=request.session_id,
    history=history
  )