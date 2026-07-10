from pydantic import BaseModel


class ChatRequest(BaseModel):
  session_id: str
  message: str


class ChatResponse(BaseModel):
  reply: str


class ResetSessionRequest(BaseModel):
  session_id: str


class ResetSessionResponse(BaseModel):
  message: str