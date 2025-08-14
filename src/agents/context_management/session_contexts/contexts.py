from typing import List, Type, Dict
from .section_context import *

S101_CONTEXT: SectionContextBase = FactsSectionContext(
    section_id=SectionID.S101,
    section_name="Purchaser's Objectives",
    facts=[
        Fact(
            name="business_need_or_driver",
            question="What specific operational issue, deficiency, or risk tied to the Purchaser's operations is prompting this procurement?",
            status=FactStatus.pending,
            answers=[]
        ),
        Fact(
            name="strategic_goals",
            question="What longer-term business or strategic objectives — such as compliance, market expansion, or performance targets — is the Purchaser aiming to achieve through this procurement?",
            status=FactStatus.pending,
            answers=[]
        ),
        Fact(
            name="intended_operational_outcomes",
            question="What tangible, measurable improvements in operations does the Purchaser expect after successful delivery (e.g. reduced downtime, improved throughput)?",
            status=FactStatus.pending,
            answers=[]
        ),
        Fact(
            name="existing_operational_issues",
            question="What known defects, inefficiencies, or operational risks in current systems or processes is this procurement meant to fix or mitigate?",
            status=FactStatus.pending,
            answers=[]
        ),
        Fact(
            name="assets_being_replaced_or_upgraded",
            question="Which existing assets, systems, or equipment will be replaced, upgraded, or decommissioned as a direct result of this procurement?",
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
        Fact(
            name="drawings_required",
            question="Are drawings required to define or illustrate the goods, and if not, what is the short reason?",
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
        Fact(
            name="tests_required",
            question="Are any tests or inspections required before the goods can be accepted by the Purchaser? If not, what is the reason they are not necessary?",
            status=FactStatus.pending,
            answers=[]
        ),
        Fact(
            name="test_scope_and_methods",
            question="What specific tests or inspections must be carried out, and which standards or test methods apply to each one?",
            status=FactStatus.pending,
            answers=[]
        ),
        Fact(
            name="responsibility_location_timing",
            question="Who will perform the required tests, who (if anyone) must witness or sign them off, and when and where will these take place — for example, at the factory, on-site, or before delivery?",
            status=FactStatus.pending,
            answers=[]
        ),
        Fact(
            name="acceptance_criteria_and_documents",
            question="What measurable pass/fail criteria apply to the tests, and what records or certificates must be provided for the goods to be accepted?",
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
        Fact(
            name="samples_required",
            question="Are samples of the goods required before manufacturing or delivery? If not, what is the reason they are not necessary?",
            status=FactStatus.pending,
            answers=[]
        ),
        Fact(
            name="sample_type_and_quantity",
            question="What type of samples must be provided — such as material swatch, component sample, mock-up, or prototype — and what quantity or size is needed for each? What specific attribute does each sample represent (e.g. colour, finish, material)?",
            status=FactStatus.pending,
            answers=[]
        ),
        Fact(
            name="submission_requirements",
            question="What are the requirements for how samples must be packaged, labelled, or delivered — including where and by when they must be submitted?",
            status=FactStatus.pending,
            answers=[]
        ),
        Fact(
            name="acceptance_procedure",
            question="How will the Purchaser decide whether to accept or reject the samples, who will review or sign off, are witnesses required, and what record will confirm the outcome?",
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
        Fact(
            name="management_approach",
            question="How will the tests and inspections be organised and coordinated — including how they are scheduled, what notice periods apply, and how communication will be handled? (Do not describe the test content.)",
            status=FactStatus.pending,
            answers=[]
        ),
        Fact(
            name="attendance_and_approvals",
            question="Which roles are required to attend or witness the tests or inspections, and which role is responsible for approving the results?",
            status=FactStatus.pending,
            answers=[]
        ),
        Fact(
            name="access_and_facilities",
            question="What arrangements are required for access to the site or factory — such as inductions, permits, or the availability of facilities and equipment?",
            status=FactStatus.pending,
            answers=[]
        ),
        Fact(
            name="records_and_submissions",
            question="What records, certificates, or reports must be submitted after testing — and what format, submission method, or location is required?",
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
        Fact(
            name="defect_reporting_process",
            question="When a defect is found during inspection, testing, or delivery, how must it be reported — who is notified, how is it reported, and are there any required timeframes?",
            status=FactStatus.pending,
            answers=[]
        ),
        Fact(
            name="correction_authority_and_plan",
            question="Who authorises the repair or replacement of a defect, and what must be agreed in advance (e.g., method statement, timing) before work starts?",
            status=FactStatus.pending,
            answers=[]
        ),
        Fact(
            name="access_and_coordination_for_rework",
            question="How will access be arranged for repair or replacement, who coordinates the logistics, and what permits or site rules apply?",
            status=FactStatus.pending,
            answers=[]
        ),
        Fact(
            name="reinspection_and_acceptance",
            question="After a defect is corrected, how will the goods be re-inspected or verified, and what records or certificates are needed for acceptance?",
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
        Fact(
            name="activities_requiring_method_statements",
            question="Which specific activities require method statements or risk assessments — for example, lifting, transport, installation, working at height, or confined space work?",
            status=FactStatus.pending,
            answers=[]
        ),
        Fact(
            name="submission_timing_and_approval",
            question="When must these documents be submitted before the activity begins, and who is responsible for reviewing and approving them?",
            status=FactStatus.pending,
            answers=[]
        ),
        Fact(
            name="formats_templates_and_platforms",
            question="Are there required formats, templates, or submission platforms that the Supplier must use for method statements or risk assessments?",
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
        Fact(
            name="hse_procedures_and_site_rules",
            question="Are there Purchaser-specific health and safety procedures or site rules the Supplier must follow — such as site entry requirements, PPE standards, inductions, working at height, hot work, or confined space rules? Provide the titles or references to the relevant documents.",
            status=FactStatus.pending,
            answers=[]
        ),
        Fact(
            name="training_permits_and_documents",
            question="What training, permits, or safety documentation must the Supplier have before starting work — for example, valid inductions, hot work permits, confined space permits, or an approved contractor HSE plan?",
            status=FactStatus.pending,
            answers=[]
        ),
        Fact(
            name="incident_reporting_requirements",
            question="How must safety incidents or near misses be reported — including who must be notified, the required timeframes, and any forms or systems that must be used?",
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
        Fact(
            name="statutory_requirements_applicable",
            question="Are there any legal or regulatory requirements that apply to the goods or their supply? If not, briefly explain why none are applicable.",
            status=FactStatus.pending,
            answers=[]
        ),
        Fact(
            name="applicable_laws_and_regulations",
            question="What laws, regulations, or industry-specific rules apply to the goods or their supply? Include the official titles and jurisdictions.",
            status=FactStatus.pending,
            answers=[]
        ),
        Fact(
            name="dutyholders_and_regulators",
            question="Which legal dutyholders or regulatory bodies must the Supplier engage with or notify, and what are their specific roles?",
            status=FactStatus.pending,
            answers=[]
        ),
        Fact(
            name="approvals_permits_and_documents",
            question="What approvals, permits, or statutory certificates are required, and at what point must they be obtained or submitted?",
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
        Fact(
            name="inspections_applicable",
            question="Will the Purchaser carry out inspections or audits of the Supplier’s safety systems? If not, what is the reason they are not required?",
            status=FactStatus.pending,
            answers=[]
        ),
        Fact(
            name="inspection_frequency_scope_and_format",
            question="How often will inspections or audits of the Supplier’s safety systems take place, and what scope or format will they follow — such as documentation checks, site visits, or formal audits?",
            status=FactStatus.pending,
            answers=[]
        ),
        Fact(
            name="required_documents_for_review",
            question="Which safety-related documents must the Supplier submit for review — for example, the HSE plan, procedures, incident logs, or training records?",
            status=FactStatus.pending,
            answers=[]
        ),
        Fact(
            name="purchaser_review_roles_and_reporting",
            question="Who on the Purchaser’s team is responsible for reviewing the safety documentation, and how will the findings or required actions be communicated to the Supplier?",
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
        Fact(
            name="training_required",
            question="Is the Supplier required to provide training to the Purchaser’s team? If not, what is the reason training is not needed?",
            status=FactStatus.pending,
            answers=[]
        ),
        Fact(
            name="training_scope_topics",
            question="What topics or subject areas must the training cover — for example, operation, safety, and maintenance?",
            status=FactStatus.pending,
            answers=[]
        ),
        Fact(
            name="delivery_method_timing_location_and_attendance",
            question="How will the training be delivered (on-site or remote), when and where will it take place, how many people will attend, and must the training be completed before Delivery or Handover?",
            status=FactStatus.pending,
            answers=[]
        ),
        Fact(
            name="trainer_qualifications_materials_and_certification",
            question="What qualifications must the trainer have, what training materials must be provided, and is any certification or sign-off required after the training is complete?",
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
        Fact(
            name="prohibitions_applicable",
            question="Are there any materials the Supplier is prohibited or restricted from using in the goods? If none apply, state 'None'.",
            status=FactStatus.pending,
            answers=[]
        ),
        Fact(
            name="scope_of_application",
            question="Do these material prohibitions apply only to the goods’ primary materials, or do they also apply to coatings, insulation, adhesives, lubricants, and packaging?",
            status=FactStatus.pending,
            answers=[]
        ),
        Fact(
            name="policy_or_standard_references",
            question="What laws, regulations, or Purchaser policies restrict the use of materials? List their titles and edition or date where known.",
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
        Fact(
            name="purchaser_rules_and_access",
            question="Are there Purchaser-specific rules the Supplier must follow, including site access restrictions or zone limits? If yes, list them.",
            status=FactStatus.pending,
            answers=[]
        ),
        Fact(
            name="working_hours_and_logistics",
            question="Are there working-hour restrictions or logistical constraints — such as delivery windows or traffic limitations — that affect how the Supplier performs the work?",
            status=FactStatus.pending,
            answers=[]
        ),
        Fact(
            name="environmental_or_permit_constraints",
            question="Are there constraints related to environmental permits, ecological sensitivity, or similar regulatory approvals that the Supplier must comply with?",
            status=FactStatus.pending,
            answers=[]
        ),
        Fact(
            name="third_party_requirements",
            question="Are there requirements imposed by other stakeholders — such as neighbours, utilities, or authorities — that the Supplier must comply with? If yes, who are they and what requirements apply?",
            status=FactStatus.pending,
            answers=[]
        ),
        Fact(
            name="legal_or_regulatory_constraints",
            question="Are there legal or regulatory conditions — such as municipal by-laws, licence or permit requirements, or road and utility permissions — that affect how the Supplier performs the work?",
            status=FactStatus.pending,
            answers=[]
        ),
        Fact(
            name="community_constraints",
            question="Are there community-related constraints the Supplier must observe — for example, noise curfews, restricted routes, school hours, event blackouts, or public notification requirements?",
            status=FactStatus.pending,
            answers=[]
        ),
        Fact(
            name="other_constraints",
            question="Are there any other constraints the Supplier must observe that do not fall under the previous categories? If yes, describe them.",
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
    SectionID.S202: SectionS202Context,
    SectionID.S301: FactsSectionContext,
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