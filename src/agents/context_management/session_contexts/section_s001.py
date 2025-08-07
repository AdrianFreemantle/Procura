from ast import List
from section_context import SectionContext, SectionID, Fact, NamedFact

SECTION_CONTEXTS: List[SectionContext] = [
    S101_CONTEXT, 
    S102_CONTEXT, 
    S103_CONTEXT
]

S101_CONTEXT: SectionContext = SectionContext(
    section=SectionID.S101,
    section_status="in_progress",
    next_question="What operational issue or inefficiency is motivating this procurement?",
    facts=[
        NamedFact(
            name="business_need_or_driver",
            data=Fact(
                description="The primary operational issue, risk, or inefficiency that motivates the procurement.",
                question="What operational issue or inefficiency is motivating this procurement?",
                priority=90,
                value=""
            )
        ),
        NamedFact(
            name="strategic_goals",
            data=Fact(
                description="Long-term objectives or strategic motivations behind the purchase (e.g. modernization, compliance, growth).",
                question="What strategic or long-term goals are driving this procurement?",
                priority=80,
                value=""
            )
        ),
        NamedFact(
            name="intended_operational_outcomes",
            data=Fact(
                description="Desired improvements from successful delivery (e.g. reduced downtime, improved safety, cost savings).",
                question="What outcomes or benefits does the Purchaser expect from this procurement?",
                priority=70,
                value=""
            )
        ),
        NamedFact(
            name="existing_operational_issues",
            data=Fact(
                description="Known limitations, risks, or challenges with current systems or processes that the procurement aims to address.",
                question="What are the current issues, risks, or inefficiencies the new goods aim to solve?",
                priority=60,
                value=""
            )
        ),
        NamedFact(
            name="assets_being_replaced_or_upgraded",
            data=Fact(
                description="Existing assets, equipment, or systems that will be replaced or upgraded as part of this procurement.",
                question="Are any existing assets being replaced or upgraded by this procurement?",
                priority=50,
                value=""
            )
        ),
        NamedFact(
            name="procurement_constraints",
            data=Fact(
                description="Internal or external constraints affecting procurement (e.g. deadlines, regulations, physical limitations).",
                question="Are there any constraints (e.g., regulatory, financial, time-based) affecting this procurement?",
                priority=40,
                value=""
            )
        )
    ]
)

S102_CONTEXT: SectionContext = SectionContext(
    section=SectionID.S102,
    section_status="in_progress",
    next_question="What are the goods called or referred to as by the Purchaser?",
    facts=[
        NamedFact(
            name="goods_common_name",
            data=Fact(
                description="The name or label by which the Purchaser refers to the goods.",
                question="What are the goods called or referred to as by the Purchaser?",
                priority=90,
                value=""
            )
        ),
        NamedFact(
            name="intended_use",
            data=Fact(
                description="What the goods will be used for in the Purchaser’s operation.",
                question="What are the goods used for in your operation?",
                priority=80,
                value=""
            )
        ),
        NamedFact(
            name="core_characteristics",
            data=Fact(
                description="Key measurable or factual attributes of the goods (e.g. type, size, model, capacity).",
                question="What are the core attributes of the goods (e.g., type, model, size, or capacity)?",
                priority=70,
                value=""
            )
        ),
        NamedFact(
            name="brand_or_origin_constraints",
            data=Fact(
                description="Whether a specific brand, manufacturer, or country of origin is preferred or required.",
                question="Is there a required or preferred brand or origin for the goods?",
                priority=60,
                value=""
            )
        ),
        NamedFact(
            name="optional_variants_or_accessories",
            data=Fact(
                description="Any optional features, accessories, or variants the Purchaser expects to be included.",
                question="Are there optional variants or accessories expected to be included with the goods?",
                priority=50,
                value=""
            )
        )
    ]
)

class DrawingReference(BaseModel):
    number: str = Field(default="", description="Drawing number or unique identifier")
    title: str = Field(default="", description="Title or name of the drawing")
    revision: str = Field(default="", description="Revision level of the drawing")
    purpose: str = Field(default="", description="Optional description of what the drawing shows or its relevance")


S103_CONTEXT: SectionContext = SectionContext(
    section=SectionID.S103,
    section_status="in_progress",
    next_question="Are there any drawings that help define or illustrate the goods?",
    facts=[
        NamedFact(
            name="drawing_list",
            data=Fact(
                description="A list of all drawings that directly relate to the goods, including number, title, and revision. Must be encoded as a JSON list of drawing objects.",
                question=(
                    "Please provide the list of drawings that show the design, arrangement, or installation of the goods. "
                    "For each drawing, include the number, title, revision, and optionally describe its purpose."
                ),
                priority=90,
                value="[]"  # Will be populated with a JSON string like '[{"number": "DWG-001", "title": "Main Layout", ...}]'
            )
        )
    ]
)