from app.services.conversation_store import get_history as store_get_history
from app.services.conversation_store import append_message as store_append_message
from app.services.conversation_store import clear_history as store_clear_history
from app.services.conversation_store import get_recent_history as store_get_recent_history

def get_history(session_id: str):
  return store_get_history(session_id)

def append_message(session_id: str, role: str, content: str):
  return store_append_message(session_id, role, content)

def clear_history(session_id: str):
  return store_clear_history(session_id)

def get_recent_history(session_id: str, limit: int = 10):
  return store_get_recent_history(session_id, limit)