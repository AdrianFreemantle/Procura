
import sqlite3
import json
from agents.context_management.interview_context import InterviewContext

class SqlLiteContextStore:
  def __init__(self, db_path: str = ":memory:"):
    self.db_path = db_path
    self._conn = None
    if db_path == ":memory:":
      self._conn = sqlite3.connect(db_path)
      self._ensure_table(self._conn)
    else:
      self._ensure_table()

  def _get_connection(self):
    if self._conn:
      return self._conn
    return sqlite3.connect(self.db_path)

  def _ensure_table(self, conn=None):
    conn = conn or self._get_connection()
    try:
      conn.execute(
        """
        CREATE TABLE IF NOT EXISTS contexts (
          context_id TEXT PRIMARY KEY,
          context_json TEXT NOT NULL
        )
        """
      )
      conn.commit()
    finally:
      if not self._conn:
        conn.close()

  def get_context(self, context_id: str) -> InterviewContext | None:
    conn = self._get_connection()
    try:
      cur = conn.execute(
        "SELECT context_json FROM contexts WHERE context_id = ?",
        (context_id,)
      )
      row = cur.fetchone()
      if row:
        data = json.loads(row[0])
        return InterviewContext.model_validate(data)
      return None
    finally:
      if not self._conn:
        conn.close()

  def store_context(self, context: InterviewContext):
    conn = self._get_connection()
    try:
      context_json = context.model_dump_json()
      conn.execute(
        "REPLACE INTO contexts (context_id, context_json) VALUES (?, ?)",
        (context.context_id, context_json)
      )
      conn.commit()
    finally:
      if not self._conn:
        conn.close()

  def remove_context(self, context_id: str):
    conn = self._get_connection()
    try:
      conn.execute(
        "DELETE FROM contexts WHERE context_id = ?",
        (context_id,)
      )
      conn.commit()
    finally:
      if not self._conn:
        conn.close()

  def close(self):
    if self._conn:
      self._conn.close()
      self._conn = None
