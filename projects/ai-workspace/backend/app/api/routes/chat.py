from fastapi import APIRouter

from app.schemas.chat import (
  ChatRequest,
  ChatResponse,
  ResetSessionRequest,
  ResetSessionResponse,
  HistoryRequest,
  HistoryResponse,
)
from app.services.chat_service import generate_reply
from app.services.conversation_store import (
  clear_history,
  get_history,
)

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
  reply = generate_reply(
    session_id=request.session_id,
    message=request.message
  )
  return ChatResponse(reply=reply)

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