from enum import Enum
from typing import List, Optional, Dict
from ..enums import *
from pydantic import BaseModel, Field


class FactStatus(str, Enum):
    pending = "pending"
    partial = "partial"
    answered = "answered"
    not_applicable = "not_applicable"
    
    def __str__(self):
        return f"{self.value}"

class SectionStatus(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    complete = "complete"

class Severity(str, Enum):
    ok = "ok"
    needs_more_detail = "needs_more_detail"

    def __str__(self):
        return f"{self.value}"

# -----------------------------
# Fact primitives
# -----------------------------
class Fact(BaseModel):
    name: str = Field(default="", description="Fact key")        
    question: str = Field(default="", description="How to ask for this fact from the user")    
    answers: List[str] = Field(default_factory=list, description="Captured answers")
    status: FactStatus = Field(default=FactStatus.pending, description="Capture state")

# -----------------------------
# Section context (generic + S101 factory)
# -----------------------------
class SectionContextBase(BaseModel):
    section_id: SectionID = Field(default=SectionID.S101)    
    section_name: str = Field(default="")
    section_status: SectionStatus = Field(default=SectionStatus.pending)
    message_to_user: Optional[str] = Field(default="", description="Next question to ask")

class FactsSectionContext(SectionContextBase):
    facts: List[Fact] = Field(default_factory=list)    
    pass

class MainContext(BaseModel):
    id: MainSectionID = Field(default=MainSectionID.S100)
    name: str = Field(default="S100 Description of the Goods")
    sections: List[SectionContextBase] = Field(default_factory=list)

# -----------------------------
# Typed structures for S102
# -----------------------------
class GoodsDescription(BaseModel):
    facts: List[Fact] = Field(default=[
        Fact(
            name="goods_common_name",
            question="What name or designation does the Purchaser use for the goods in contracts and related documents?",
            status=FactStatus.pending,
            answers=[]
        ),
        Fact(
            name="goods_description",
            question="How would the purchaser describe the goods?",
            status=FactStatus.pending,
            answers=[]
        ),
        Fact(
            name="intended_use",
            question="What is the high-level operational purpose or function of the goods within the Purchaser's operations?",
            status=FactStatus.pending,
            answers=[]
        )
    ])


class SectionS102Context(SectionContextBase):
    section_id: SectionID = Field(default=SectionID.S102)
    goods_descriptions: List[GoodsDescription] = Field(default_factory=list)    

# -----------------------------
# Typed structures for S103
# -----------------------------

class DrawingReference(BaseModel):
    number: str = Field(default="", description="Unique drawing number or identifier.")
    title: str = Field(default="", description="Formal drawing title as per engineering/procurement records.")
    revision: str = Field(default="", description="Current revision level or code.")
    purpose: str = Field(default="", description="Short note on relevance (e.g., layout, fabrication, installation).")
    file_name: str = Field(default="", description="Uploaded file name if applicable.")

class DrawingList(BaseModel):
    description: str = Field(default="", description="Short summary of the drawing set (e.g., 'General arrangements and electrical schematics').")
    items: List[DrawingReference] = Field(default_factory=list, description="Drawings that visually define or clarify the goods.")

class SectionS103Context(SectionContextBase):
    section_id: SectionID = Field(default=SectionID.S103)
    drawing_list: DrawingList = Field(default_factory=DrawingList, description="A structured list of drawings used to support the description of the goods.")
