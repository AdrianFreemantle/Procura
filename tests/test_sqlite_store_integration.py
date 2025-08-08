import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pytest
from agents.context_management.persistence.sqlite_store import SqlLiteContextStore
from agents.context_management.interview_context import InterviewContext
from agents.context_management.session_contexts.section_context import SectionContextBase, SectionID

def make_sample_context(context_id="test-id"):
  section = SectionContextBase(section_id=SectionID.S101, section_status="pending", next_question="Q1", facts=[])
  ctx = InterviewContext(context_id=context_id, context_name="Test", section_id=SectionID.S101, sections=[section], conversation_history=[])
  return ctx

def test_store_and_get_context():
  store = SqlLiteContextStore(db_path=":memory:")
  ctx = make_sample_context()
  store.store_context(ctx)
  loaded = store.get_context(ctx.context_id)
  assert loaded is not None
  assert loaded.context_id == ctx.context_id
  assert loaded.sections[0].section_id == ctx.sections[0].section_id
  store.close()

def test_remove_context():
  store = SqlLiteContextStore(db_path=":memory:")
  ctx = make_sample_context()
  store.store_context(ctx)
  store.remove_context(ctx.context_id)
  assert store.get_context(ctx.context_id) is None
  store.close()

def test_overwrite_context():
  store = SqlLiteContextStore(db_path=":memory:")
  ctx = make_sample_context()
  store.store_context(ctx)
  ctx.context_name = "Updated"
  store.store_context(ctx)
  loaded = store.get_context(ctx.context_id)
  assert loaded.context_name == "Updated"
  store.close()
