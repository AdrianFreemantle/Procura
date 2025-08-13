import sqlite3
import json
from datetime import datetime
from typing import List, Dict, Optional, Any
from agents.context_management.interview_context import InterviewContext
import logging
import threading

logger = logging.getLogger(__name__)

class SqlLiteContextStore:
  def __init__(self, db_path: str = ":memory:"):
    self.db_path = db_path
    self._conn = None
    self._lock = threading.Lock()
    if db_path == ":memory:":
      # Allow use across worker threads (Gradio) and protect with a lock
      self._conn = sqlite3.connect(db_path, check_same_thread=False)
      self._ensure_table(self._conn)
    else:
      self._ensure_table()
    logger.debug("SqlLiteContextStore initialized (db_path=%s, in_memory=%s)", db_path, db_path == ":memory:")

  def _get_connection(self):
    if self._conn:
      return self._conn
    return sqlite3.connect(self.db_path)

  def _ensure_table(self, conn=None):
    conn = conn or self._get_connection()
    try:
      with self._lock:
        conn.execute(
          """
          CREATE TABLE IF NOT EXISTS contexts (
            context_id INTEGER PRIMARY KEY AUTOINCREMENT,
            context_name TEXT NOT NULL,
            context_status TEXT NOT NULL DEFAULT 'empty',
            context_json TEXT NOT NULL,
            last_updated DATETIME NOT NULL
          )
          """
        )
        conn.commit()
      logger.debug("Ensured 'contexts' table exists")
    finally:
      if not self._conn:
        conn.close()

  def get_context(self, context_id: int) -> InterviewContext | None:
    conn = self._get_connection()
    try:
      logger.debug("Fetching context id=%s", context_id)
      with self._lock:
        cur = conn.execute(
          "SELECT context_json FROM contexts WHERE context_id = ?",
          (context_id,)
        )
        row = cur.fetchone()
      if row:
        data = json.loads(row[0])
        context = InterviewContext.model_validate(data)
        
        logger.debug("Fetched context id=%s name='%s' status=%s", context.context_id, context.context_name, context.context_status)
        return context
      logger.warning("Context id=%s not found", context_id)
      return None
    finally:
      if not self._conn:
        conn.close()

  def store_context(self, context: InterviewContext) -> int:
    """Store context and return the context_id (auto-assigned for new contexts)"""
    conn = self._get_connection()
    try:
      now = datetime.now().isoformat()
      with self._lock:
        if context.context_id is None:
          # Insert new context
          logger.debug("Inserting new context name='%s' status=%s", context.context_name, context.context_status)
          cur = conn.execute(
            "INSERT INTO contexts (context_name, context_status, context_json, last_updated) VALUES (?, ?, ?, ?)",
            (context.context_name, context.context_status, "", now)
          )
          context_id = cur.lastrowid
          context.context_id = context_id
          # Now serialize with the assigned ID
          context_json = context.model_dump_json()
          # Update with the serialized JSON containing the correct ID
          conn.execute(
            "UPDATE contexts SET context_json = ? WHERE context_id = ?",
            (context_json, context_id)
          )
          logger.debug("Inserted context id=%s", context_id)
        else:
          # Update existing context - serialize with existing ID
          logger.debug("Updating context id=%s name='%s' status=%s", context.context_id, context.context_name, context.context_status)
          context_json = context.model_dump_json()
          conn.execute(
            "UPDATE contexts SET context_name = ?, context_status = ?, context_json = ?, last_updated = ? WHERE context_id = ?",
            (context.context_name, context.context_status, context_json, now, context.context_id)
          )
          context_id = context.context_id
        conn.commit()
      return context_id
    finally:
      if not self._conn:
        conn.close()

  def remove_context(self, context_id: int):
    conn = self._get_connection()
    try:
      logger.debug("Removing context id=%s", context_id)
      with self._lock:
        conn.execute(
          "DELETE FROM contexts WHERE context_id = ?",
          (context_id,)
        )
        conn.commit()
    finally:
      if not self._conn:
        conn.close()

  def list_contexts(self, current_context_id: int = None) -> List[Dict[str, Any]]:
    """Returns list of contexts with id, name, status, and last_updated, ordered by last_updated desc.
    Filters out 'empty' contexts except for the current_context_id (union approach)."""
    conn = self._get_connection()
    try:
      logger.debug("Listing contexts (current_context_id=%s)", current_context_id)
      with self._lock:
        if current_context_id is not None:
          # Union approach: get active/archived contexts + current context (even if empty)
          cur = conn.execute(
            """
            SELECT context_id, context_name, context_status, last_updated 
            FROM contexts 
            WHERE context_status != 'empty' OR context_id = ?
            ORDER BY last_updated DESC
            """,
            (current_context_id,)
          )
        else:
          # No current context, just return active/archived contexts
          cur = conn.execute(
            """
            SELECT context_id, context_name, context_status, last_updated 
            FROM contexts 
            WHERE context_status != 'empty'
            ORDER BY last_updated DESC
            """
          )
        rows = cur.fetchall()
      logger.debug("Listed %d contexts", len(rows))
      return [
        {
          "context_id": row[0],
          "context_name": row[1],
          "context_status": row[2],
          "last_updated": row[3]
        }
        for row in rows
      ]
    finally:
      if not self._conn:
        conn.close()

  def close(self):
    with self._lock:
      if self._conn:
        self._conn.close()
        self._conn = None
        logger.debug("SqlLiteContextStore connection closed")
