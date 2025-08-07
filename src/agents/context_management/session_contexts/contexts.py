from typing import List, Literal, Type, Dict
from pydantic import BaseModel, Field
from .section_context import GenericSectionContext, SectionID, Fact, NamedFact, SectionContextBase

S101_CONTEXT: SectionContextBase = GenericSectionContext(
    section_id=SectionID.S101,
    section_status="in_progress",
    next_question="",
    facts=[
        NamedFact(
            name="business_need_or_driver",
            data=Fact(
                description="The core operational problem, deficiency, or risk prompting this procurement. This should be specific, measurable, and clearly linked to the Purchaser’s operations.",
                question="What specific operational issue, inefficiency, or risk is driving the need for this procurement?",
                value=""
            )
        ),
        NamedFact(
            name="strategic_goals",
            data=Fact(
                description="The longer-term business or strategic objectives the Purchaser intends to achieve through this procurement. Examples include regulatory compliance, expansion into new markets, or achieving specific performance targets.",
                question="What longer-term business or strategic goals is the Purchaser aiming to achieve with this procurement?",
                value=""
            )
        ),
        NamedFact(
            name="intended_operational_outcomes",
            data=Fact(
                description="Tangible improvements the Purchaser expects to realise after successful delivery. These must be framed as measurable operational results (e.g. reduced downtime, lower maintenance costs, improved throughput).",
                question="What specific outcomes or improvements does the Purchaser expect to achieve through this procurement?",
                value=""
            )
        ),
        NamedFact(
            name="existing_operational_issues",
            data=Fact(
                description="Any known defects, inefficiencies, or operational risks in current systems or processes that this procurement is intended to fix or mitigate.",
                question="What known issues or shortcomings with current operations or equipment is this procurement intended to address?",
                value=""
            )
        ),
        NamedFact(
            name="assets_being_replaced_or_upgraded",
            data=Fact(
                description="Any existing assets (e.g. equipment, machinery, tools, infrastructure) that will be replaced, upgraded, or decommissioned as a direct result of this procurement.",
                question="Are there specific assets, systems, or equipment that this procurement will replace or upgrade?",
                value=""
            )
        ),
        NamedFact(
            name="procurement_constraints",
            data=Fact(
                description="Any internal or external limitations affecting the procurement. These may include regulatory deadlines, funding windows, space limitations, or coordination with other projects.",
                question="Are there any constraints — such as regulatory deadlines, funding limits, or site limitations — that affect how or when this procurement must occur?",
                value=""
            )
        )
    ]
)
S102_CONTEXT: SectionContextBase = GenericSectionContext(
    section_id=SectionID.S102,
    section_status="in_progress",
    next_question="What name or label does the Purchaser commonly use to refer to the goods being procured?",
    facts=[
        NamedFact(
            name="goods_common_name",
            data=Fact(
                description="The internal name, designation, or label by which the Purchaser identifies the goods. This should reflect how the goods are referred to in internal documents, procurement records, or day-to-day usage.",
                question="What name or label does the Purchaser commonly use to refer to the goods being procured?",
                value=""
            )
        ),
        NamedFact(
            name="intended_use",
            data=Fact(
                description="The specific operational purpose or function the goods will perform within the Purchaser’s business. This must be framed as an outcome or use case, not a technical specification.",
                question="What specific operational function will the goods perform once delivered?",
                value=""
            )
        ),
        NamedFact(
            name="core_characteristics",
            data=Fact(
                description="The factual and measurable attributes that define the goods. This includes type, capacity, model, dimensions, configuration, or any other property necessary to identify what is being procured.",
                question="What are the key measurable characteristics of the goods (such as type, size, model, or capacity)?",
                value=""
            )
        ),
        NamedFact(
            name="brand_or_origin_constraints",
            data=Fact(
                description="Any constraints or requirements relating to the brand, manufacturer, or country of origin. This includes situations where only specific suppliers or jurisdictions are acceptable due to technical, regulatory, or policy reasons.",
                question="Is there a required or preferred brand, manufacturer, or country of origin for the goods?",
                value=""
            )
        ),
        NamedFact(
            name="optional_variants_or_accessories",
            data=Fact(
                description="Any expected or permitted accessories, variants, or optional components that may be included with the goods. This includes non-essential items that the Purchaser still expects or desires.",
                question="Are there any optional accessories, variants, or add-ons that the Purchaser expects to be included?",
                value=""
            )
        )
    ]
)

class DrawingReference(BaseModel):
    number: str = Field(
        default="", 
        description="The unique drawing number or identifier used in procurement, manufacturing, or assembly."
    )
    title: str = Field(
        default="", 
        description="The formal title or label of the drawing as referenced in engineering or procurement records."
    )
    revision: str = Field(
        default="", 
        description="The current revision level or code of the drawing that indicates its version or update status."
    )
    purpose: str = Field(
        default="", 
        description="A short statement of the drawing’s relevance (e.g., layout, specification, installation)."
    )


class DrawingList(BaseModel):
    description: str = Field(
        default="", 
        description="A statement summarizing the scope or role of the drawing set (e.g. 'General arrangements and electrical schematics')."
    )
    items: List[DrawingReference] = Field(
        default_factory=list,
        description="A list of referenced drawings that visually define or clarify the goods being procured."
    )


class SectionS103Context(SectionContextBase):
    section_id: Literal[SectionID.S103] = SectionID.S103
    description: str = Field(
        default="", 
        description="A concise and factual description of the goods being procured, suitable for use in legal drafting."
    )
    drawing_list: DrawingList = Field(
        default_factory=DrawingList,
        description="A structured list of drawings used to support the description of the goods."
    )


S103_CONTEXT: SectionContextBase = SectionS103Context(
    section_status="in_progress",
    next_question="Are there any drawings that define or illustrate the goods being procured?",
    facts=[
        NamedFact(
            name="any_drawings",
            data=Fact(
                description="Indicates whether any engineering or technical drawings are used to define, clarify, or specify the goods. These may include layouts, schematics, or component diagrams.",
                question="Are there any drawings that define or illustrate the goods being procured?",
                value=""
            )
        )
    ]
)


SECTION_CONTEXT_TYPES: Dict[SectionID, Type[SectionContextBase]] = {
    SectionID.S101: GenericSectionContext,
    SectionID.S102: GenericSectionContext,
    SectionID.S103: SectionS103Context,
}

CONTEXTS: List[SectionContextBase] = [
    S101_CONTEXT, 
    S102_CONTEXT, 
    S103_CONTEXT
]
