conversation_store: dict[str, list[dict[str, str]]] = {}

def get_history(session_id: str) -> list[dict[str, str]]:
  ...

def append_message(session_id: str, role: str, content: str) -> None:
  ...