import sqlite3
from pathlib import Path

DB_PATH = Path("data/phoenix.db")

def get_connection():
  return sqlite3.connect(DB_PATH)

def get_history(session_id: str) -> list[dict[str, str]]:
  conn = get_connection()
  cursor = conn.cursor()

  cursor.execute(
    """
    SELECT role, content
    FROM conversation_messages
    WHERE session_id = ?
    ORDER BY id ASC
    """,
    (session_id,)
  )

  rows = cursor.fetchall()

  conn.close()
  
  return [
    {
      "role": role,
      "content": content,
    }
    for role, content in rows
  ]

def append_message(
  session_id: str,
  role: str,
  content: str
) -> None:
  conn = get_connection()
  cursor = conn.cursor()

  cursor.execute(
    f"""
    INSERT INTO conversation_messages
    (
      session_id,
      role,
      content
    )
    VALUES (?, ?, ?)
    """,
    (
      session_id,
      role,
      content,
    )
  )
  conn.commit()
  conn.close()

def clear_history(session_id: str) -> None:
  conn = get_connection()
  cursor = conn.cursor()

  cursor.execute(
    """
    DELETE FROM conversation_messages
    WHERE session_id = ?
    """,
    (session_id,)
  )

  conn.commit()
  conn.close()

def init_db():
  DB_PATH.parent.mkdir(exist_ok=True)
  conn = sqlite3.connect(DB_PATH)
  cursor = conn.cursor()
  cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS conversation_messages (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      session_id TEXT NOT NULL,
      role TEXT NOT NULL,
      content TEXT NOT NULL,
      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """
  )
  conn.commit()
  conn.close()

conversation_store: dict[str, list[dict[str, str]]] = {}


init_db()