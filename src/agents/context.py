from pydantic import BaseModel, Field
from typing import List, Literal
from agents.enums import SectionID 

SectionStatus = Literal["not_started", "in_progress", "complete", "not_applicable"]

from pydantic import BaseModel, Field
from typing import Literal

class SectionContext(BaseModel):
    section_status: Literal["in_progress", "complete"] = Field(
        default="in_progress", 
        description="Completion status of the section based on captured facts."
    )

    next_question: str = Field(
        default="", 
        description="Next question to ask"
    )

    facts

class S101_Facts(BaseModel):
    section_status: Literal["in_progress", "complete"] = Field(
        default="in_progress", 
        description="Completion status of the section based on captured facts."
    )

    business_need_or_driver: str = Field(
        default="", 
        description="The primary operational issue, risk, or inefficiency that motivates the procurement."
    )

    strategic_goals: str = Field(
        default="", 
        description="Long-term objectives or strategic motivations behind the purchase (e.g. modernization, compliance, growth)."
    )

    intended_operational_outcomes: str = Field(
        default="", 
        description="Desired improvements from successful delivery (e.g. reduced downtime, improved safety, cost savings)."
    )

    existing_operational_issues: str = Field(
        default="", 
        description="Known limitations, risks, or challenges with current systems or processes that the procurement aims to address."
    )

    assets_being_replaced_or_upgraded: str = Field(
        default="", 
        description="Existing assets, equipment, or systems that will be replaced or upgraded as part of this procurement."
    )

    procurement_constraints: str = Field(
        default="", 
        description="Internal or external constraints affecting procurement (e.g. deadlines, regulations, physical limitations)."
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
    next_question: str = Field(default="Start the interview by greeting the user. Ask if they have any background information they would like to share.", description="Next question to ask")
    current_section: SectionID = Field(default=SectionID.S101, description="Current section of the NEC4 SCC contract")
    s101_facts: S101_Facts = Field(default_factory=S101_Facts, description="Purchaser's Objectives")
    s102_facts: S102_Facts = Field(default_factory=S102_Facts, description="Description of the Goods")
    s103_facts: S103_Facts = Field(default_factory=S103_Facts, description="Drawings")