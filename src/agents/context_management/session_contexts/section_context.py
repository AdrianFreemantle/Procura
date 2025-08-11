from enum import Enum
from typing import Final, List, Optional
from ..enums import SectionID
from pydantic import BaseModel, Field

# -----------------------------
# Enums (single source of truth)
# -----------------------------
class FactStatus(str, Enum):
    pending = "pending"
    partial = "partial"
    answered = "answered"
    not_applicable = "not_applicable"

class SectionStatus(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    complete = "complete"

class Severity(str, Enum):
    ok = "ok"
    needs_more_detail = "needs_more_detail"

# -----------------------------
# Fact primitives
# -----------------------------
class NamedFact(BaseModel):
    name: str = Field(default="", description="Fact key")
    answers: List[str] = Field(default_factory=list, description="Captured answers")
    description: str = Field(default="", description="What this fact represents")
    question: str = Field(default="", description="How to ask for this fact from the user")    
    status: FactStatus = Field(default=FactStatus.pending, description="Capture state")

# -----------------------------
# Section context (generic + S101 factory)
# -----------------------------
class SectionContextBase(BaseModel):
    section_id: SectionID = Field(default=SectionID.S101)
    section_title: str = Field(default="")
    section_purpose: str = Field(default="")
    interview_guidance: str = Field(default="")
    section_status: SectionStatus = Field(default=SectionStatus.pending)
    facts: List[NamedFact] = Field(default_factory=list)    
    message_to_user: Optional[str] = Field(default="", description="Next question to ask")

class GenericSectionContext(SectionContextBase):
    pass