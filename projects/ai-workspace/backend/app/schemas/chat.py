from pydantic import BaseModel


class ChatRequest(BaseModel):
  session_id: str
  message: str
  metadata: dict[str, str] = {}

class ChatResponse(BaseModel):
  reply: str

class ErrorResponse(BaseModel):
  error: str

class ResetSessionRequest(BaseModel):
  session_id: str


class ResetSessionResponse(BaseModel):
  message: str


class HistoryRequest(BaseModel):
  session_id: str


class HistoryResponse(BaseModel):
  session_id: str
  history: list[dict[str, str]]