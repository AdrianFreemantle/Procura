from typing import List, Type, Dict
from .section_context import *

S101_CONTEXT: SectionContextBase = FactsSectionContext(
    section_id=SectionID.S101,    
    facts=[
        NamedFact(
            name="business_need_or_driver",
            description="Operational problem, deficiency, or risk prompting this procurement, tied to Purchaser operations.",
            question="What specific operational issue, deficiency, or risk is prompting this procurement, in the context of your operations?",            
            status=FactStatus.pending,
            answers=[]
        ),
        NamedFact(
            name="strategic_goals",
            description="The longer-term business or strategic objectives the Purchaser intends to achieve through this procurement. Examples include regulatory compliance, expansion into new markets, or achieving specific performance targets.",
            question="What longer-term business or strategic goals is the Purchaser aiming to achieve with this procurement?",
            status=FactStatus.pending,
            answers=[]
        ),
        NamedFact(
            name="intended_operational_outcomes",
            description="Tangible improvements the Purchaser expects to realise after successful delivery. These must be framed as measurable operational results (e.g. reduced downtime, lower maintenance costs, improved throughput).",
            question="What specific outcomes or improvements does the Purchaser expect to achieve through this procurement?",
            status=FactStatus.pending,
            answers=[]
        ),
        NamedFact(
            name="existing_operational_issues",
            description="Any known defects, inefficiencies, or operational risks in current systems or processes that this procurement is intended to fix or mitigate.",
            question="What known issues or shortcomings with current operations or equipment is this procurement intended to address?",
            status=FactStatus.pending,
            answers=[]
        ),
        NamedFact(
            name="assets_being_replaced_or_upgraded",
            description="Any existing assets (e.g. equipment, machinery, tools, infrastructure) that will be replaced, upgraded, or decommissioned as a direct result of this procurement.",
            question="Are there specific assets, systems, or equipment that this procurement will replace or upgrade?",
            status=FactStatus.pending,
            answers=[]        
        )
    ]
)

S102_CONTEXT: SectionContextBase = SectionS102Context(
    section_id=SectionID.S102,    
    section_status=SectionStatus.pending,
    goods_descriptions= [GoodsDescription()]
)

S103_CONTEXT: SectionContextBase = SectionS103Context(
    section_status=SectionStatus.pending,
    facts=[
        NamedFact(
            name="drawings_required",
            description="Whether drawings are required to define or illustrate the goods. If not required, provide a short reason.",
            question="Are drawings required to define or illustrate the goods? If not, briefly state why.",
            status=FactStatus.pending,
            answers=[]
        )
    ]
)

S104_CONTEXT: SectionContextBase = FactsSectionContext(
    section_id=SectionID.S104,  
    section_name="Tests and Inspections",  
    section_status=SectionStatus.pending,
    facts=[
        NamedFact(
            name="tests_required",
            description="Whether any tests or inspections are required before the goods are accepted. If not required, provide a brief reason.",
            question="Are any tests or inspections required before the goods are accepted? If not, briefly state why.",
            status=FactStatus.pending,
            answers=[]
        ),
        NamedFact(
            name="test_scope_and_methods",
            description="Concise list of required tests or inspections, including the applicable standard or test method for each.",
            question="What tests or inspections must be carried out, and which standards or test methods apply?",
            status=FactStatus.pending,
            answers=[]
        ),
        NamedFact(
            name="responsibility_location_timing",
            description="Who performs the tests, who (if anyone) must witness or sign off, and when and where they take place (e.g., factory, site, pre-delivery).",
            question="Who will carry out the tests, who must witness or sign off (if applicable), and when and where will they take place?",
            status=FactStatus.pending,
            answers=[]
        ),
        NamedFact(
            name="acceptance_criteria_and_documents",
            description="Measurable pass/fail criteria for each test and the required records or certificates for acceptance.",
            question="What are the pass/fail criteria for these tests, and what documents or certificates are required for acceptance?",
            status=FactStatus.pending,
            answers=[]
        )
    ]
)

S105_CONTEXT: SectionContextBase = FactsSectionContext(
    section_id=SectionID.S105,
    section_name="Samples",
    section_status=SectionStatus.pending,
    facts=[
        NamedFact(
            name="samples_required",
            description="Whether samples of the goods are required before manufacturing or delivery. If not required, give a brief reason.",
            question="Does the Purchaser require samples of any goods before manufacturing or delivery? If not, briefly state why.",
            status=FactStatus.pending,
            answers=[]
        ),
        NamedFact(
            name="sample_type_and_quantity",
            description="What samples must be submitted (e.g., material swatch, component sample, mock-up, prototype) and the quantity or size for each. Indicate what attribute the sample represents (e.g., colour, finish, material, construction).",
            question="What type of samples must be submitted (for example, material swatch, component sample, mock-up), and how many of each?",
            status=FactStatus.pending,
            answers=[]
        ),
        NamedFact(
            name="submission_requirements",
            description="Any rules for packaging, labelling, or delivery of samples, including where and by when they must be submitted.",
            question="Are there any rules about how samples must be packaged, labelled, or delivered?",
            status=FactStatus.pending,
            answers=[]
        ),
        NamedFact(
            name="acceptance_procedure",
            description="How acceptance of samples will be decided, who will review or sign off, any required witnesses, and what record will confirm acceptance or rejection.",
            question="How will acceptance be decided, who will review, and what record will confirm acceptance or rejection?",
            status=FactStatus.pending,
            answers=[]
        )
    ]
)

S106_CONTEXT: SectionContextBase = FactsSectionContext(
    section_id=SectionID.S106,
    section_name="Management of Tests and Inspections",
    section_status=SectionStatus.pending,
    facts=[
        NamedFact(
            name="management_approach",
            description="How tests and inspections will be organised and coordinated, including scheduling process, notice periods, and communication method. Do not include test content.",
            question="How will the tests and inspections be managed (scheduling, notice periods, coordination and communication)?",
            status=FactStatus.pending,
            answers=[]
        ),
        NamedFact(
            name="attendance_and_approvals",
            description="Roles required to attend or witness tests/inspections and the role responsible for approving results.",
            question="Who must attend or witness the tests or inspections, and who approves the results?",
            status=FactStatus.pending,
            answers=[]
        ),
        NamedFact(
            name="access_and_facilities",
            description="Arrangements for access to the site or factory, including any inductions, permits, or facilities/equipment to be made available.",
            question="How will access to the site or factory be arranged, and are any inductions, permits, or facilities required?",
            status=FactStatus.pending,
            answers=[]
        ),
        NamedFact(
            name="records_and_submissions",
            description="Records, certificates, or reports to be submitted after testing, including required format and method/location for submission.",
            question="What records or certificates must be submitted afterwards, and in what format or where should they be submitted?",
            status=FactStatus.pending,
            answers=[]
        )
    ]
)

S107_CONTEXT: SectionContextBase = FactsSectionContext(
    section_id=SectionID.S107,
    section_name="Correcting Defects",
    section_status=SectionStatus.pending,
    facts=[
        NamedFact(
            name="defect_reporting_process",
            description="How a defect is reported when found during inspection, testing, or delivery: who is notified, how it is reported, and any timeframes.",
            question="What process must be followed to notify a defect found during inspection, testing, or delivery?",
            status=FactStatus.pending,
            answers=[]
        ),
        NamedFact(
            name="correction_authority_and_plan",
            description="Who authorises repair or replacement and what must be agreed before correction starts (for example, method statement and timing).",
            question="Who authorises repair or replacement, and what must be agreed before correction starts?",
            status=FactStatus.pending,
            answers=[]
        ),
        NamedFact(
            name="access_and_coordination_for_rework",
            description="How access will be arranged for repair or replacement, who coordinates logistics, and any required permits or site rules.",
            question="Who manages access and coordination for rework, and what arrangements or permits are required?",
            status=FactStatus.pending,
            answers=[]
        ),
        NamedFact(
            name="reinspection_and_acceptance",
            description="How corrected goods will be re-inspected or verified and what records or certificates are required for acceptance.",
            question="How will repairs or replacements be re-inspected or verified before final acceptance, and what records are required?",
            status=FactStatus.pending,
            answers=[]
        )
    ]
)


S108_CONTEXT: SectionContextBase = FactsSectionContext(
    section_id=SectionID.S108,
    section_name="Health and Safety Requirements",
    section_status=SectionStatus.pending,
    facts=[
        NamedFact(
            name="hse_procedures_and_site_rules",
            description="Purchaser-specific H&S procedures or site rules the Supplier must follow (for example, site entry rules, PPE standards, inductions, working at height, hot work, confined spaces). Provide titles or references to the relevant documents.",
            question="Are there Purchaser-specific health and safety procedures or site rules the Supplier must follow? State their titles or references.",
            status=FactStatus.pending,
            answers=[]
        ),
        NamedFact(
            name="training_permits_and_documents",
            description="Training, permits, or safety documentation required before the Supplier may work (for example, valid inductions, hot work permits, confined space permits, contractor HSE plan).",
            question="Does the Purchaser require specific training, permits, or safety documentation before the Supplier may work? Specify what is required.",
            status=FactStatus.pending,
            answers=[]
        ),
        NamedFact(
            name="incident_reporting_requirements",
            description="How safety incidents and near misses must be reported, including who to notify, required timeframes, and any form or system to be used.",
            question="How must safety incidents or near misses be reported? Include who to notify and the required timeframe.",
            status=FactStatus.pending,
            answers=[]
        )
    ]
)

S109_CONTEXT: SectionContextBase = FactsSectionContext(
    section_id=SectionID.S109,
    section_name="Method Statements",
    section_status=SectionStatus.pending,
    facts=[
        NamedFact(
            name="activities_requiring_method_statements",
            description="Specific activities that require method statements or risk assessments (for example, lifting, transport, installation, working at height, confined space).",
            question="Are there specific activities that require method statements or risk assessments? If yes, list them.",
            status=FactStatus.pending,
            answers=[]
        ),
        NamedFact(
            name="submission_timing_and_approval",
            description="When the documents must be submitted before the activity, and who will review and approve them.",
            question="When must the documents be submitted, and who approves them?",
            status=FactStatus.pending,
            answers=[]
        ),
        NamedFact(
            name="formats_templates_and_platforms",
            description="Any required formats, templates, or submission platforms for method statements or risk assessments.",
            question="Are there any formats, templates, or submission platforms the Supplier must use?",
            status=FactStatus.pending,
            answers=[]
        )
    ]
)

S110_CONTEXT: SectionContextBase = FactsSectionContext(
    section_id=SectionID.S110,
    section_name="Statutory Requirements",
    section_status=SectionStatus.pending,
    facts=[
        NamedFact(
            name="statutory_requirements_applicable",
            description="Whether legal or regulatory requirements apply to the goods or their supply. If not applicable, provide a brief reason.",
            question="Are there any legal or regulatory requirements the Supplier must comply with when providing the goods? If not, briefly state why.",
            status=FactStatus.pending,
            answers=[]
        ),
        NamedFact(
            name="applicable_laws_and_regulations",
            description="Titles and jurisdictions of laws or regulations that apply, including any industry-specific rules.",
            question="Which laws or regulations apply to the goods or their supply? Include the jurisdiction and official titles.",
            status=FactStatus.pending,
            answers=[]
        ),
        NamedFact(
            name="dutyholders_and_regulators",
            description="Legal dutyholders or regulators the Supplier must work with or notify, and their roles.",
            question="Are there legal dutyholders or regulators the Supplier must work with or notify? Who are they and what is their role?",
            status=FactStatus.pending,
            answers=[]
        ),
        NamedFact(
            name="approvals_permits_and_documents",
            description="Required approvals, permits, or statutory certificates and when they must be obtained or submitted.",
            question="What approvals, permits, or statutory certificates are required, and when must they be obtained or submitted?",
            status=FactStatus.pending,
            answers=[]
        )
    ]
)

S111_CONTEXT: SectionContextBase = FactsSectionContext(
    section_id=SectionID.S111,
    section_name="Inspections of Safety Procedures",
    section_status=SectionStatus.pending,
    facts=[
        NamedFact(
            name="inspections_applicable",
            description="Whether the Purchaser will carry out inspections or audits of the Supplier’s safety systems. If not applicable, give a brief reason.",
            question="Will the Purchaser carry out inspections or audits of the Supplier’s safety systems? If not, briefly state why.",
            status=FactStatus.pending,
            answers=[]
        ),
        NamedFact(
            name="inspection_frequency_scope_and_format",
            description="How often inspections will take place and the scope or format they will follow (for example, documentation checks, site visits, formal audits).",
            question="How often will inspections take place, and what scope or format will they follow?",
            status=FactStatus.pending,
            answers=[]
        ),
        NamedFact(
            name="required_documents_for_review",
            description="Safety documents the Supplier must submit for review (for example, HSE plan, procedures, incident logs, training records).",
            question="What safety documents must the Supplier submit for review?",
            status=FactStatus.pending,
            answers=[]
        ),
        NamedFact(
            name="purchaser_review_roles_and_reporting",
            description="Who on the Purchaser’s team performs the review and how findings or actions will be communicated to the Supplier.",
            question="Who on the Purchaser’s team performs the review, and how will findings be communicated?",
            status=FactStatus.pending,
            answers=[]
        )
    ]
)

S112_CONTEXT: SectionContextBase = FactsSectionContext(
    section_id=SectionID.S112,
    section_name="Training Requirements",
    section_status=SectionStatus.pending,
    facts=[
        NamedFact(
            name="training_required",
            description="Whether the Supplier must provide training to the Purchaser’s team. If not required, provide a brief reason.",
            question="Must the Supplier provide training to the Purchaser’s team? If not, briefly state why.",
            status=FactStatus.pending,
            answers=[]
        ),
        NamedFact(
            name="training_scope_topics",
            description="Topics or scope the training must cover, for example operation, safety, and maintenance.",
            question="What topics must the training cover (for example, operation, safety, maintenance)?",
            status=FactStatus.pending,
            answers=[]
        ),
        NamedFact(
            name="delivery_method_timing_location_and_attendance",
            description="How the training will be delivered and scheduled, including delivery method (on-site or remote), when it will occur, where it will take place, and how many people will attend. Indicate if training must be completed before Delivery or Handover.",
            question="When and where should the training take place, how will it be delivered (on-site or remote), how many people will attend, and must it be completed before Delivery or Handover?",
            status=FactStatus.pending,
            answers=[]
        ),
        NamedFact(
            name="trainer_qualifications_materials_and_certification",
            description="Required qualifications of the trainer, training materials to be provided, and whether certification or sign-off is required after completion.",
            question="What qualifications must the trainer have, what training materials must be provided, and is any certification or sign-off required?",
            status=FactStatus.pending,
            answers=[]
        )
    ]
)

class SpecificationGrouping(BaseModel):
    answer: str = Field(default="", description="How requirements will be organised"),
    question: str = Field(default="", description="How requirements will be organised: single block, by discipline, by component, or by system/assembly.")    


class SpecificationItem(BaseModel):
    subject: str = Field(default="", description="What the requirement applies to (for example, 'General', 'Mechanical', 'Electrical', 'Operation and control', 'Components' e.g. motors, panels, etc., 'Safety requirements'.")
    requirements: List[str] = Field(default_factory=list, description="Requirements provided as a list of statements.")

# --- Section context for S201 (context metadata limited to section_id and section_status) ---

class SectionS201Context(SectionContextBase):
    section_id: SectionID = Field(default=SectionID.S201)
    section_name: str = Field(default="Specifications")
    section_status: SectionStatus = Field(default=SectionStatus.pending)
    grouping_option: SpecificationGrouping = Field(default_factory=SpecificationGrouping)
    specfication_items: List[SpecificationItem] = Field(default_factory=list, description="Flat list of specifications/requirements (no grouping).")

S201_CONTEXT: SectionContextBase = SectionS201Context(    
    section_id=SectionID.S201,
    section_name="Specifications",
    section_status=SectionStatus.pending,
    grouping_option=SpecificationGrouping(
        answer="", 
        question="How will requirements be organised: single block, by discipline, by component, or by system/assembly."),
    specfication_items=[
        SpecificationItem(subject="Example General Requirements (For LLM context only, remove before submitting)", 
            requirements=[
                "Is designed to meet the process design criteria provided by the Purchaser.",
                "Is compatible with the existing plant infrastructure and control systems.",
                "Meets or exceed industry standards, codes, and regulations relevant to their respective categories.",
                "Is constructed, tested, and documented in compliance with applicable quality assurance and control standards. ",
                "Is constructed from materials suitable for the intended application and environment.",
                "Is designed to withstand the operating conditions, including temperature, pressure, and corrosion resistance.",
                "Complies with all health, safety and environmental statutory requirements.",
                "Undergoes rigorous testing and inspection to verify compliance with specifications.",
                "Is packaged to prevent damage during transit and storage.",
                "Is properly label and handling instructions provided."
            ]),
        SpecificationItem(subject="General Requirements", requirements=[]), 
        SpecificationItem(subject="Safety Requirements", requirements=[])]
    
)

# S202 – Deleterious and Hazardous Materials: Schema (context has only section_id and section_status)
# --- Typed models for S202 ---

class ProhibitedMaterial(BaseModel):
    name: str = Field(default="", description="Material, chemical, or substance not permitted (for example, asbestos, lead-based paint, PCBs).")
    category: str = Field(default="", description="Category or type (for example, insulation, coating, refrigerant, adhesive).")
    scope: str = Field(default="", description="Where the prohibition applies (for example, in the goods, coatings, insulation, lubricants, packaging).")
    legal_basis: str = Field(default="", description="Law, regulation, or standard that restricts the material (title and edition/date if known).")
    policy_reference: str = Field(default="", description="Purchaser policy or blacklist reference, if any.")
    threshold: str = Field(default="", description="If restricted (not outright banned), state the limit (for example, '≤0.1% w/w').")
    notes: str = Field(default="", description="Clarifications or exceptions, such as permitted substitutes or conditional use.")

# --- Section context for S202 (only section_id and section_status, plus facts and structured content) ---

class SectionS202Context(SectionContextBase):
    section_id: SectionID = Field(default=SectionID.S202)
    section_name: str = Field(default="Deleterious and Hazardous Materials")
    section_status: SectionStatus = Field(default=SectionStatus.pending)
    prohibited_materials: List[ProhibitedMaterial] = Field(default_factory=list, description="Materials prohibited or restricted for use in the goods.")

S202_CONTEXT: SectionContextBase = SectionS202Context(
    section_id=SectionID.S202,
    section_name="Deleterious and Hazardous Materials",
    section_status=SectionStatus.pending,
    facts=[
        NamedFact(
            name="prohibitions_applicable",
            description="Whether any materials are prohibited or restricted for use in the goods. If none apply, this should explicitly state 'None'.",
            question="Are there materials the Supplier must not use in the goods? If none apply, state 'None'.",
            status=FactStatus.pending,
            answers=[]
        ),
        NamedFact(
            name="scope_of_application",
            description="Whether the prohibitions apply only to the goods’ primary materials or also to coatings, insulation, adhesives, lubricants, and packaging.",
            question="Do these prohibitions apply only to the goods’ primary materials, or also to coatings, insulation, adhesives, lubricants, and packaging?",
            status=FactStatus.pending,
            answers=[]
        ),
        NamedFact(
            name="policy_or_standard_references",
            description="Titles of any laws, regulations, or Purchaser policies that restrict materials (include edition/date where known).",
            question="List any laws, regulations, or Purchaser policies that restrict materials (include titles and edition/date where known).",
            status=FactStatus.pending,
            answers=[]
        )
    ]
)

S301_CONTEXT: SectionContextBase = FactsSectionContext(
    section_id=SectionID.S301,
    section_name="General Constraints",
    section_status=SectionStatus.pending,
    facts=[
        NamedFact(
            name="purchaser_rules_and_access",
            description="Purchaser-specific rules or site access/zone limits the Supplier must follow.",
            question="Are there Purchaser-specific rules or access or zone limits the Supplier must follow? If yes, list them.",
            status=FactStatus.pending,
            answers=[]
        ),
        NamedFact(
            name="working_hours_and_logistics",
            description="Working-hour limits and traffic or delivery constraints that affect how the Supplier performs the work.",
            question="Are there working-hour limits or traffic or delivery constraints (for example, no deliveries after 18:00)? If yes, list them.",
            status=FactStatus.pending,
            answers=[]
        ),
        NamedFact(
            name="environmental_or_permit_constraints",
            description="Constraints arising from environmental permits, ecological sensitivity, or similar approvals.",
            question="Do environmental permits or ecological sensitivities impose constraints? If yes, summarise them.",
            status=FactStatus.pending,
            answers=[]
        ),
        NamedFact(
            name="third_party_requirements",
            description="Requirements imposed by other stakeholders or authorities that the Supplier must comply with.",
            question="Must the Supplier comply with requirements from neighbours or authorities? If yes, who are they and what requirements apply?",
            status=FactStatus.pending,
            answers=[]
        ),
        NamedFact(
            name="legal_or_regulatory_constraints",
            description="Legal or regulatory constraints that affect how the Supplier performs the work (for example, municipal by-laws, licence or permit conditions, road or utility permissions).",
            question="Are there legal or regulatory constraints that affect how the Supplier performs the work (for example, municipal by-laws, licence or permit conditions, road or utility permissions)? If yes, list them.",
            status=FactStatus.pending,
            answers=[]
        ),
        NamedFact(
            name="community_constraints",
            description="Community-related constraints the Supplier must observe (for example, noise curfews, restricted routes, school hours, event blackouts, public notification requirements).",
            question="Are there community-related constraints the Supplier must observe (for example, noise curfews, restricted routes, school hours, event blackouts, public notification requirements)? If yes, list them.",
            status=FactStatus.pending,
            answers=[]
        ),
        NamedFact(
            name="other_constraints",
            description="Other constraints the Supplier must observe (for example, noise curfews, restricted routes, school hours, event blackouts, public notification requirements).",
            question="Are there other constraints the Supplier must observe (for example, noise curfews, restricted routes, school hours, event blackouts, public notification requirements)? If yes, list them.",
            status=FactStatus.pending,
            answers=[]
        )
    ]
)



SECTION_CONTEXT_TYPES: Dict[SectionID, Type[SectionContextBase]] = {
    SectionID.S101: FactsSectionContext,
    SectionID.S102: SectionS102Context,
    SectionID.S103: SectionS103Context,
    SectionID.S104: FactsSectionContext,
    SectionID.S105: FactsSectionContext,
    SectionID.S106: FactsSectionContext,
    SectionID.S107: FactsSectionContext,
    SectionID.S108: FactsSectionContext,
    SectionID.S109: FactsSectionContext,
    SectionID.S110: FactsSectionContext,
    SectionID.S111: FactsSectionContext,
    SectionID.S112: FactsSectionContext,
    SectionID.S201: SectionS201Context,
}

CONTEXTS: List[SectionContextBase] = [
    S101_CONTEXT, 
    S102_CONTEXT, 
    S103_CONTEXT,
    S104_CONTEXT,
    S105_CONTEXT,
    S106_CONTEXT,
    S107_CONTEXT,
    S108_CONTEXT,
    S109_CONTEXT,
    S110_CONTEXT,
    S111_CONTEXT,
    S112_CONTEXT,
    S201_CONTEXT,
    S202_CONTEXT,
    S301_CONTEXT    
]

MAIN_CONTEXT_S100 = MainContext(
    id=MainSectionID.S100,
    name="Description of the Goods",
    sections=[S101_CONTEXT, S102_CONTEXT, S103_CONTEXT, S104_CONTEXT, S105_CONTEXT, S106_CONTEXT, S107_CONTEXT, S108_CONTEXT, S109_CONTEXT, S110_CONTEXT, S111_CONTEXT, S112_CONTEXT, S201_CONTEXT]
)

MAIN_CONTEXT_S200 = MainContext(
    id=MainSectionID.S200,
    name="Specifications",
    sections=[S201_CONTEXT, S202_CONTEXT]
)

MAIN_CONTEXT_S300 = MainContext(
    id=MainSectionID.S300,
    name="Constraints on How the Supplier Provides the Goods",
    sections=[S301_CONTEXT]
)

MAIN_CONTEXTS: List[MainContext] = [
    MAIN_CONTEXT_S100,
    MAIN_CONTEXT_S200,
    MAIN_CONTEXT_S300
]