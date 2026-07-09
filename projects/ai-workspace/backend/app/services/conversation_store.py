conversation_store: dict[str, list[dict[str, str]]] = {}

def get_history(session_id: str) -> list[dict[str, str]]:
  return conversation_store.get(session_id, [])

def append_message(session_id: str, role: str, content: str) -> None:
  if session_id not in conversation_store:
    conversation_store[session_id] = []

  conversation_store[session_id].append(
    {
      "role": role,
      "content": content,
    }
  )

def clear_history(session_id: str) -> None:
  if session_id in conversation_store:
    del conversation_store[session_id]