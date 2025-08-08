import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pytest
from agents.chat_manager import ChatManager
from agents.context_management.interview_context import InterviewContext
from agents.context_management.persistence.sqlite_store import SqlLiteContextStore


def _stub_chat_manager() -> ChatManager:
  # Ensure OpenAI client in agents initializes without real key
  os.environ.setdefault("OPENAI_API_KEY", "test")
  cm = ChatManager()
  # Stub external agents to avoid network calls
  cm.facts_agent.evaluate = lambda ctx: ctx.get_current_section()

  def fake_interview(ctx):
    # Simulate a single streamed assistant turn
    def _gen():
      ctx.conversation_append("assistant", "ok")
      yield ctx.conversation_history
    return _gen()

  cm.interviewer_agent.interview = fake_interview
  return cm


def test_create_and_list_current_empty():
  cm = _stub_chat_manager()
  try:
    ctx = cm.create_new_context()
    cm.save_context(ctx)
    lst = cm.list_contexts()
    # Current context should be included even if status is 'empty'
    assert any(item["context_id"] == cm.current_context_id for item in lst)
  finally:
    cm.context_store.close()


def test_first_message_promotes_to_active_and_persists():
  cm = _stub_chat_manager()
  try:
    ctx = cm.create_new_context()
    cm.save_context(ctx)
    # Send first message and exhaust the generator to trigger save
    for _ in cm.chat("hello"):
      pass
    assert cm.persisted_context.context_status == "active"
    assert cm.persisted_context.context_id is not None
    # Conversation should include user and assistant messages
    roles = [m["role"] for m in cm.persisted_context.conversation_history]
    assert roles.count("user") >= 1
    assert roles.count("assistant") >= 1
  finally:
    cm.context_store.close()


def test_switch_between_contexts_and_history():
  cm = _stub_chat_manager()
  try:
    # Context 1
    c1 = cm.create_new_context()
    cm.save_context(c1)
    for _ in cm.chat("hello c1"):
      pass
    c1_id = cm.current_context_id

    # Context 2
    c2 = cm.create_new_context()
    cm.save_context(c2)
    c2_id = cm.current_context_id

    # Switch back to context 1
    ctx = cm.switch_context(c1_id)
    assert cm.current_context_id == c1_id
    assert any(msg["content"].startswith("hello c1") for msg in ctx.conversation_history if msg["role"] == "user")

    # Switch to context 2
    ctx = cm.switch_context(c2_id)
    assert cm.current_context_id == c2_id
  finally:
    cm.context_store.close()


def test_list_filters_empty_non_current():
  cm = _stub_chat_manager()
  try:
    # c1 (empty, saved)
    c1 = cm.create_new_context()
    cm.save_context(c1)
    c1_id = cm.current_context_id

    # c2 becomes current (empty, saved)
    c2 = cm.create_new_context()
    cm.save_context(c2)
    c2_id = cm.current_context_id

    lst = cm.list_contexts()
    # Only current empty (c2) should show; c1 is empty and not current -> filtered out
    ids = [x["context_id"] for x in lst]
    assert c2_id in ids
    assert c1_id not in ids
  finally:
    cm.context_store.close()


def test_store_thread_safety_sanity():
  # Use a single shared in-memory store across threads
  store = SqlLiteContextStore(db_path=":memory:")
  try:
    from concurrent.futures import ThreadPoolExecutor

    def create_one(name: str):
      ctx = InterviewContext(context_name=name)
      return store.store_context(ctx)

    with ThreadPoolExecutor(max_workers=4) as ex:
      ids = list(ex.map(create_one, [f"T{i}" for i in range(8)]))

    assert len(ids) == 8
    assert len(set(ids)) == 8
    assert all(isinstance(i, int) and i > 0 for i in ids)
  finally:
    store.close()
