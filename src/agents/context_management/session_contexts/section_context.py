from pydantic import BaseModel, Field
from typing import List, Literal
from ..enums import SectionID

# -----------------------------
# FACT MODEL
# -----------------------------

class Fact(BaseModel):
    value: str = Field(default="", description="Captured fact from the Purchaser")
    description: str = Field(default="", description="What this fact represents or explains")
    question: str = Field(default="", description="Question to ask the Purchaser to obtain this fact")
    optional: bool = Field(default=True, description="Whether this fact is required to complete the section")
    priority: int = Field(default=0, description="Helps prioritise question order")

# -----------------------------
# WRAPPER FOR FACT NAME
# -----------------------------

class NamedFact(BaseModel):
    name: str = Field(default="", description="Name/key of the fact (used for lookup)")
    data: Fact = Field(default_factory=Fact, description="Fact metadata and value")


# -----------------------------
# SECTION CONTEXT MODEL
# -----------------------------

class SectionContextBase(BaseModel):
    section_id: SectionID = Field(default=SectionID.S101, description="Which contract section this context represents")
    section_status: Literal["pending", "in_progress", "complete"] = Field(default="pending", description="Whether all facts are complete")
    next_question: str = Field(default="", description="Next interview question to ask")
    facts: List[NamedFact] = Field(default_factory=list, description="List of facts to capture for this section") 

class GenericSectionContext(SectionContextBase):
    pass

