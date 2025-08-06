from pydantic import BaseModel, Field
from typing import List, Literal
from agents.enums import SectionID 

SectionStatus = Literal["not_started", "in_progress", "complete", "not_applicable"]

class S101_Facts(BaseModel):
    section_status: SectionStatus = Field(default="in_progress", description="Completion status for Section")
    
    business_problem_or_need: str = Field(
        default="", 
        description="The primary business problem, inefficiency, or risk the Purchaser is aiming to solve by acquiring these goods"
    )
    
    strategic_objectives: str = Field(
        default="", 
        description="High-level goals or motivations driving the procurement (e.g., compliance, capacity expansion, modernisation)"
    )
    
    intended_outcomes_or_benefits: str = Field(
        default="", 
        description="Tangible or intangible benefits expected from successful delivery (e.g., cost savings, safety improvements, reduced downtime)"
    )
    
    current_pain_points_or_limitations: str = Field(
        default="", 
        description="Key operational challenges or limitations in the existing system that the new goods are intended to address"
    )
    
    assets_being_replaced_or_upgraded: str = Field(
        default="", 
        description="Whether this purchase is replacing/upgrading existing assets, and if so, a brief description of what is being replaced"
    )
    
    constraints_driving_procurement: str = Field(
        default="", 
        description="External or internal constraints (e.g., regulatory deadlines, space limitations, performance thresholds) that shape the procurement need"
    )

class S102_Facts(BaseModel):
    section_status: SectionStatus = Field(default="not_started", description="Completion status for Section")
    goods_name: str = Field(default="", description="Common name or designation for the goods (e.g., 'high-voltage switchgear')")
    goods_category_or_type: str = Field(default="", description="Classification or type (e.g., 'electrical equipment', 'mechanical component')")
    intended_use: str = Field(default="", description="Purpose or application for which the goods are required")
    basic_characteristics: str = Field(default="", description="Key physical or functional characteristics such as size, capacity, power rating, or model")
    included_components_or_accessories: str = Field(default="", description="Any parts, accessories, or subcomponents included as part of the goods")
    manufacturer_or_origin: str = Field(default="", description="Brand, model, or manufacturer if specified or constrained")
    variants_or_options: str = Field(default="", description="Permitted or required variants, models, or configuration options")
    visual_description_or_identifiers: str = Field(default="", description="Any visual features, labels, or markings that distinguish the goods")

class DrawingReference(BaseModel):
    section_status: SectionStatus = Field(default="not_started", description="Completion status for Section")
    drawing_title: str = Field(default="", description="Title or name of the drawing")
    drawing_number: str = Field(default="", description="Unique drawing or document number")
    drawing_purpose: str = Field(default="", description="Purpose or type (e.g., layout, fabrication, connection)")
    revision: str = Field(default="", description="Revision or version identifier")
    source_or_origin: str = Field(default="", description="Originating party or system (e.g., Purchaser, Supplier, third-party consultant)")
    file_link_or_location: str = Field(default="", description="Optional path or URL to the drawing file if managed digitally")

class S103_Facts(BaseModel):
    section_status: SectionStatus = Field(default="not_started", description="Completion status for Section")
    drawing_list: List[DrawingReference] = Field(default_factory=list, description="List of drawings, diagrams, or schematics relevant to the goods")
    general_notes: str = Field(default="", description="General notes about drawings, including format expectations or coordination notes")

class Context(BaseModel):
    next_question: str = Field(default="What is the strategic reason for procuring the goods?", description="Next question to ask")
    current_section: SectionID = Field(default=SectionID.S101, description="Current section of the NEC4 SCC contract")
    s101_facts: S101_Facts = Field(default_factory=S101_Facts, description="Purchaser's Objectives")
    s102_facts: S102_Facts = Field(default_factory=S102_Facts, description="Description of the Goods")
    s103_facts: S103_Facts = Field(default_factory=S103_Facts, description="Drawings")

