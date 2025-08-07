from pydantic import BaseModel, Field
from typing import List, Literal
from section_context import SectionID

# -----------------------------
# FACT MODEL
# -----------------------------

class Fact(BaseModel):
    value: str = Field(default="", description="Captured fact from the Purchaser")
    description: str = Field(..., description="What this fact represents or explains")
    question: str = Field(..., description="Question to ask the Purchaser to obtain this fact")
    optional: bool = Field(default=False, description="Whether this fact is required to complete the section")
    priority: int = Field(default=0, description="Helps prioritise question order")

# -----------------------------
# WRAPPER FOR FACT NAME
# -----------------------------

class NamedFact(BaseModel):
    name: str = Field(..., description="Name/key of the fact (used for lookup)")
    data: Fact = Field(..., description="Fact metadata and value")


# -----------------------------
# SECTION CONTEXT MODEL
# -----------------------------

class SectionContext(BaseModel):
    section: SectionID = Field(..., description="Which contract section this context represents")
    facts: List[NamedFact] = Field(..., description="List of facts to capture for this section")
    next_question: str = Field(default="", description="Next interview question to ask")
    section_status: Literal["in_progress", "complete"] = Field(default="in_progress", description="Whether all facts are complete")
