from fastapi import APIRouter

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat_service import generate_reply

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
  reply = generate_reply(
    session_id=request.session_id,
    message=request.message
  )
  return ChatResponse(reply=reply)