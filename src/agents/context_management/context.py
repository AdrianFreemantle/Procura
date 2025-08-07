from pydantic import BaseModel, Field
from typing import List, Literal
from agents.context_management.enums import SectionID 
from typing import Optional 

SectionStatus = Literal["not_started", "in_progress", "complete", "not_applicable"]

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
    section_status: Literal["in_progress", "complete"] = Field(
        default="in_progress",
        description="Completion status of the section based on captured facts."
    )

    goods_name: str = Field(
        default="",
        description="Common name or designation for the goods (e.g. 'high-voltage switchgear')."
    )

    goods_category_or_type: str = Field(
        default="",
        description="Classification or general type of goods (e.g. 'electrical equipment', 'mechanical component')."
    )

    intended_use: str = Field(
        default="",
        description="Intended application or functional purpose for which the goods are being procured."
    )

    basic_characteristics: str = Field(
        default="",
        description="Key physical or performance characteristics (e.g. size, capacity, voltage, power rating)."
    )

    included_components_or_accessories: str = Field(
        default="",
        description="Any accessories, subcomponents, or ancillary items included in the supply."
    )

    manufacturer_or_origin: str = Field(
        default="",
        description="Specified or preferred manufacturer, brand, or country of origin (if constrained)."
    )

    variants_or_options: str = Field(
        default="",
        description="Permitted variations or selectable options (e.g. colour, model, configuration)."
    )

    visual_description_or_identifiers: str = Field(
        default="",
        description="Distinctive visual markings, features, or labels used to identify the goods."
    )

class DrawingReference(BaseModel):
    drawing_title: str = Field(
        default="",
        description="Title or descriptive name of the drawing or document."
    )
    drawing_number: str = Field(
        default="",
        description="Unique identifier or reference number for the drawing."
    )
    drawing_purpose: str = Field(
        default="",
        description="Purpose or category of the drawing (e.g. layout, fabrication, connection)."
    )
    revision: str = Field(
        default="",
        description="Revision or version code of the drawing."
    )
    source_or_origin: str = Field(
        default="",
        description="Party responsible for creating or issuing the drawing (e.g. Purchaser, Supplier, Consultant)."
    )
    file_link_or_location: str = Field(
        default="",
        description="Optional file path, URL, or document location if managed digitally."
    )

class S103_Facts(BaseModel):
    section_status: Literal["in_progress", "complete"] = Field(
        default="in_progress",
        description="Completion status of the section based on captured facts."
    )
    drawing_list: List[DrawingReference] = Field(
        default_factory=list,
        description="List of drawings, schematics, or diagrams relevant to the goods being supplied."
    )
    general_notes: str = Field(
        default="",
        description="Additional notes or expectations related to the drawings (e.g. formats, coordination, references)."
    )

class S104_Facts(BaseModel):
    section_status: Literal["in_progress", "complete"] = Field(
        default="in_progress",
        description="Completion status of the section based on captured facts."
    )

    are_tests_required: str = Field(
        default="",
        description="Whether any tests or inspections are required for acceptance of the goods."
    )

    test_description: str = Field(
        default="",
        description="Description of the specific tests or inspections to be carried out."
    )

    responsible_party: str = Field(
        default="",
        description="Party responsible for conducting the tests or inspections (e.g. Supplier, Purchaser, third-party)."
    )

    test_location: str = Field(
        default="",
        description="Where the tests or inspections will take place (e.g. on-site, factory, lab)."
    )

    test_timing: str = Field(
        default="",
        description="When the tests or inspections will occur (e.g. before dispatch, on delivery, post-installation)."
    )

    test_standards_or_methods: str = Field(
        default="",
        description="Any applicable standards, procedures, tolerances, or test methods that must be followed."
    )

    acceptance_criteria: str = Field(
        default="",
        description="Pass/fail thresholds or conditions under which the goods will be accepted."
    )

    documentation_required: str = Field(
        default="",
        description="Whether documentation (e.g. certificates, test reports) must be submitted and what type."
    )

class S105_Facts(BaseModel):
    section_status: Literal["in_progress", "complete"] = Field(
        default="in_progress",
        description="Completion status of the section based on captured facts."
    )

    are_samples_required: str = Field(
        default="",
        description="Whether the Supplier must submit any physical samples of the goods for approval before supply or fabrication."
    )

    sample_type_or_description: str = Field(
        default="",
        description="Description of the sample(s) required, such as type, component, material, or finish."
    )

    review_or_acceptance_criteria: str = Field(
        default="",
        description="Criteria or method by which the Purchaser will review and accept or reject the sample."
    )

    packaging_or_delivery_requirements: str = Field(
        default="",
        description="Instructions related to packaging, labelling, or delivery of the sample(s)."
    )

    is_sample_retained_as_standard: str = Field(
        default="",
        description="Whether the approved sample will be retained and used as the benchmark for evaluating the delivered goods."
    )

class S106_Facts(BaseModel):
    section_status: Literal["in_progress", "complete"] = Field(
        default="in_progress",
        description="Completion status of the section based on captured facts."
    )

    test_coordination_and_planning: str = Field(
        default="",
        description="How tests and inspections will be scheduled, coordinated, and managed, including logistics and planning responsibilities."
    )

    attendance_and_approval_roles: str = Field(
        default="",
        description="Who must be present during tests, who is responsible for approving results, and any required witness protocols."
    )

    documentation_and_reporting_process: str = Field(
        default="",
        description="How results will be documented, reported, and submitted, including forms, formats, and timing."
    )

    site_access_or_logistics_requirements: str = Field(
        default="",
        description="Access arrangements, location constraints, or logistical requirements for conducting the tests."
    )

    required_certificates_or_templates: str = Field(
        default="",
        description="Any specified records, templates, certificates, or sign-off forms required as part of test or inspection management."
    )

class S107_Facts(BaseModel):
    section_status: Literal["in_progress", "complete"] = Field(
        default="in_progress",
        description="Completion status of the section based on captured facts."
    )

    defect_reporting_process: str = Field(
        default="",
        description="How defects are reported, including the process, responsible parties, and notification method."
    )

    access_for_corrections: str = Field(
        default="",
        description="How access to the goods or site will be arranged to enable defect correction or repair."
    )

    corrective_action_responsibilities: str = Field(
        default="",
        description="Who is responsible for approving and carrying out corrective actions or repairs."
    )

    reinspection_or_acceptance_method: str = Field(
        default="",
        description="How the correction will be verified (e.g., retesting, certification, visual check)."
    )

class S108_Facts(BaseModel):
    section_status: Literal["in_progress", "complete"] = Field(
        default="in_progress",
        description="Completion status of the section based on captured facts."
    )

    purchaser_specific_hse_rules: str = Field(
        default="",
        description="Any Purchaser-specific health, safety, or environmental (HSE) rules beyond general legal compliance."
    )

    site_access_or_safety_protocols: str = Field(
        default="",
        description="Protocols for site access, PPE requirements, or specific procedures for working safely on the Purchaser’s site."
    )

    incident_reporting_or_supervision_requirements: str = Field(
        default="",
        description="Requirements for incident reporting, near-miss logs, or supervisory oversight expected from the Supplier."
    )

    required_training_or_certifications: str = Field(
        default="",
        description="Mandatory training, qualifications, or safety certifications required for Supplier personnel."
    )

    hse_documentation_or_references: str = Field(
        default="",
        description="Formal safety documentation or references to Purchaser HSE policies, manuals, or procedures."
    )


class S109_Facts(BaseModel):
    section_status: Literal["in_progress", "complete"] = Field(
        default="in_progress",
        description="Completion status of the section based on captured facts."
    )

    activities_requiring_method_statements: str = Field(
        default="",
        description="List of activities requiring method statements or risk assessments (e.g., lifting, hot work, confined spaces)."
    )

    submission_timing_or_deadlines: str = Field(
        default="",
        description="When the Supplier must submit method statements prior to performing the activity (e.g., number of days in advance)."
    )

    purchaser_review_or_approval_process: str = Field(
        default="",
        description="Details of who will review and approve the method statements and how the approval process works."
    )

    format_or_template_requirements: str = Field(
        default="",
        description="Any specific requirements regarding the structure, content, or templates to be used for method statements."
    )

    purchaser_procedures_or_references: str = Field(
        default="",
        description="Links or references to Purchaser safety procedures or workflow documents relevant to the approval of method statements."
    )

class S110_Facts(BaseModel):
    section_status: Literal["in_progress", "complete"] = Field(
        default="in_progress",
        description="Completion status of the section based on captured facts."
    )

    applicable_legal_or_regulatory_requirements: str = Field(
        default="",
        description="National laws or industry-specific regulations that apply to the goods or their supply (e.g., CE marking, hazardous materials)."
    )

    named_statutory_dutyholders: str = Field(
        default="",
        description="Any required legal dutyholders that must be informed, consulted, or approved (e.g., inspectors, regulators)."
    )

    required_statutory_documents_or_approvals: str = Field(
        default="",
        description="Permits, certifications, or legal notices required by law prior to or during supply."
    )

    jurisdiction_specific_considerations: str = Field(
        default="",
        description="Any regional or country-specific obligations that affect the goods or delivery process."
    )

class S111_Facts(BaseModel):
    section_status: Literal["in_progress", "complete"] = Field(
        default="in_progress",
        description="Completion status of the section based on captured facts."
    )

    purchaser_intends_to_inspect_supplier_safety_procedures: str = Field(
        default="",
        description="Whether the Purchaser plans to inspect, audit, or review the Supplier’s safety procedures during the contract."
    )

    safety_documents_required_for_inspection: str = Field(
        default="",
        description="Types of safety-related documentation the Supplier must provide for inspection or audit (e.g. safety plans, procedures, checklists)."
    )

    inspection_frequency_and_format: str = Field(
        default="",
        description="How often inspections will occur and their format (e.g. site visit, document review)."
    )

    responsible_purchaser_roles: str = Field(
        default="",
        description="Individuals or roles on the Purchaser’s team responsible for conducting the inspections or audits."
    )

class S112_Facts(BaseModel):
    section_status: Literal["in_progress", "complete"] = Field(
        default="in_progress",
        description="Completion status of the section based on captured facts."
    )

    supplier_required_to_provide_training: str = Field(
        default="",
        description="Whether the Supplier must provide training to the Purchaser’s personnel."
    )

    training_topics_or_scope: str = Field(
        default="",
        description="Topics the training must cover (e.g. operation, maintenance, safety, handover procedures)."
    )

    training_timing_and_location: str = Field(
        default="",
        description="When and where the training will occur, and any timing dependencies (e.g. before handover)."
    )

    number_of_attendees_or_target_roles: str = Field(
        default="",
        description="Estimated number of attendees and/or the roles or functions that need to be trained."
    )

    training_materials_and_delivery_method: str = Field(
        default="",
        description="Expectations for training materials (manuals, slides), instructor qualifications, delivery format (in-person, online), etc."
    )

    completion_criteria_or_certification: str = Field(
        default="",
        description="How training completion will be validated (e.g. sign-off, certificate, test)."
    )


class SpecificationGroup(BaseModel):
    group_title: str = Field(
        default="",
        description="Descriptive title for the specification group (e.g. 'General Requirements', 'Electrical Components', 'Protective Coatings')."
    )
    specification_text: str = Field(
        default="",
        description="Technical specification details for this group, including standards, materials, tolerances, etc."
    )
    referenced_documents_or_standards: List[str] = Field(
        default_factory=list,
        description="List of document names, standard numbers, or datasheet references that apply to this group."
    )

class S201_Facts(BaseModel):
    section_status: Literal["in_progress", "complete"] = Field(
        default="in_progress",
        description="Completion status of the section based on captured facts."
    )

    grouping_approach: str = Field(
        default="",
        description="How specifications are organized (e.g. by discipline, component, assembly, or general categories)."
    )

    general_specifications: str = Field(
        default="",
        description="Any overarching specifications that apply to all goods (e.g. material standards, finish requirements, codes of compliance)."
    )

    specification_groups: List[SpecificationGroup] = Field(
        default_factory=list,
        description="List of detailed specification entries grouped by discipline, system, or component."
    )

    uploaded_specifications: List[str] = Field(
        default_factory=list,
        description="List of filenames, document titles, or upload references containing supporting specifications or datasheets."
    )

class S202_Facts(BaseModel):
    section_status: Literal["in_progress", "complete"] = Field(
        default="in_progress",
        description="Completion status of the section based on captured facts."
    )

    prohibited_materials: str = Field(
        default="",
        description="Materials, chemicals, or components explicitly prohibited from use (e.g., asbestos, lead-based paints, VOC-heavy coatings)."
    )

    internal_blacklists_or_standards: str = Field(
        default="",
        description="Any internal Purchaser policies or sustainability standards that restrict material use."
    )

    statutory_or_regulatory_references: str = Field(
        default="",
        description="Relevant statutory or environmental regulations that govern material restrictions (e.g., REACH, RoHS, local environmental laws)."
    )

    uploaded_material_restrictions: List[str] = Field(
        default_factory=list,
        description="List of uploaded documents or references to material blacklists, compliance lists, or Purchaser standards."
    )

class S301_Facts(BaseModel):
    section_status: Literal["in_progress", "complete"] = Field(
        default="in_progress",
        description="Completion status of the section based on captured facts."
    )

    legal_or_permit_constraints: str = Field(
        default="",
        description="Legal obligations, permits, or statutory conditions affecting how the Supplier may perform the work (e.g. heritage protection, road usage)."
    )

    environmental_or_community_constraints: str = Field(
        default="",
        description="Environmental or community-related limitations such as noise restrictions, working hours, or protected zones."
    )

    purchaser_internal_policies: str = Field(
        default="",
        description="Purchaser’s internal rules or policies that constrain the Supplier’s conduct or access."
    )

    third_party_or_neighbouring_party_constraints: str = Field(
        default="",
        description="Restrictions imposed by adjacent property owners, tenants, or local authorities that affect how the Supplier may operate."
    )

    plain_language_examples: List[str] = Field(
        default_factory=list,
        description="Examples of constraints written in simple terms (e.g. 'no deliveries before 7am', 'avoid access road B')."
    )

class S301_Facts(BaseModel):
    section_status: Literal["in_progress", "complete"] = Field(
        default="in_progress",
        description="Completion status of the section based on captured facts."
    )

    internal_policy_constraints: str = Field(
        default="",
        description="Purchaser’s internal policies or community expectations that restrict how or when the Supplier performs work."
    )

    environmental_constraints: str = Field(
        default="",
        description="Environmental limitations such as noise restrictions, working hours, or protection zones."
    )

    legal_or_permit_based_constraints: str = Field(
        default="",
        description="Legal duties, permit conditions, or statutory obligations that constrain Supplier conduct (e.g. heritage access, municipal road use)."
    )

    third_party_constraints: str = Field(
        default="",
        description="Restrictions imposed by neighbouring properties, tenants, or authorities that impact Supplier operations."
    )

    plain_language_examples: List[str] = Field(
        default_factory=list,
        description="Examples of constraints expressed in everyday language (e.g. 'no deliveries before 7am', 'Supplier must avoid access road B')."
    )

class S302_Facts(BaseModel):
    section_status: Literal["in_progress", "complete"] = Field(
        default="in_progress",
        description="Completion status of the section based on captured facts."
    )

    confidentiality_scope: str = Field(
        default="",
        description="Details on what types of information must be kept confidential (e.g. technical, commercial, site-specific)."
    )

    publicity_restrictions: str = Field(
        default="",
        description="Restrictions on publicity, media communications, or social media postings by the Supplier."
    )

    subcontractor_obligations: str = Field(
        default="",
        description="Whether Subcontractors must sign NDAs or adhere to confidentiality terms."
    )

    post_contract_restrictions: str = Field(
        default="",
        description="Rules about handling or retaining confidential information after project completion."
    )

    specific_prohibited_uses: List[str] = Field(
        default_factory=list,
        description="Examples of prohibited uses like site photography, sharing drawings with third parties, or reusing technical data elsewhere."
    )

class S303_Facts(BaseModel):
    section_status: Literal["in_progress", "complete"] = Field(
        default="in_progress",
        description="Completion status for the section"
    )

    security_clearance_required: bool = Field(
        default=False,
        description="Whether any form of background checks or security clearance is required before access."
    )

    clearance_details: str = Field(
        default="",
        description="Description of the type of clearance, who conducts it, and how it must be verified."
    )

    induction_required: bool = Field(
        default=False,
        description="Whether any site-specific induction or training is mandatory before access."
    )

    induction_details: str = Field(
        default="",
        description="Details about induction timing, content, or delivery method (e.g. online, onsite)."
    )

    access_controls: List[str] = Field(
        default_factory=list,
        description="Access control mechanisms such as ID badges, biometric systems, or escort policies."
    )

    access_restrictions: str = Field(
        default="",
        description="Time-of-day restrictions, area-specific access rules, or movement limitations within the premises."
    )

class S304_Facts(BaseModel):
    section_status: Literal["in_progress", "complete"] = Field(
        default="in_progress",
        description="Completion status for the section"
    )

    protection_during_handling: str = Field(
        default="",
        description="Description of protection methods used during loading, unloading, or internal movement (e.g. padding, straps, forklift guidance)."
    )

    interim_storage_protection: str = Field(
        default="",
        description="Measures to prevent damage or degradation during storage (e.g. weatherproofing, climate control, separation by type)."
    )

    packaging_requirements: List[str] = Field(
        default_factory=list,
        description="Required packaging, crating, wrapping, or labeling standards to prevent harm."
    )

    protection_until_installation: bool = Field(
        default=False,
        description="Whether protective measures must remain in place until inspection, handover, or installation."
    )

    on_site_protection_measures: str = Field(
        default="",
        description="Specific site-based measures like fencing, protective covers, vibration dampening, or access restrictions."
    )

class S305_Facts(BaseModel):
    section_status: Literal["in_progress", "complete"] = Field(
        default="in_progress",
        description="Completion status for the section"
    )

    union_or_labour_policies: str = Field(
        default="",
        description="Any union, labour, or industrial relations policies the Supplier must follow (e.g. site agreements, dispute protocols)."
    )

    site_induction_or_briefing_required: bool = Field(
        default=False,
        description="Whether the Supplier must attend site induction or industrial relations briefings."
    )

    local_hiring_expectations: str = Field(
        default="",
        description="Any local or community hiring obligations or expectations (e.g. quotas, preferences)."
    )

    known_dispute_sensitivities: List[str] = Field(
        default_factory=list,
        description="Known issues, disputes, or sensitivities from prior projects that the Supplier should be aware of."
    )

    subcontractor_constraints: str = Field(
        default="",
        description="Any restrictions or expectations related to the Supplier’s use of subcontractors or labour brokers."
    )

class S306_Facts(BaseModel):
    section_status: Literal["in_progress", "complete"] = Field(
        default="in_progress",
        description="Completion status for the section"
    )

    generates_waste: bool = Field(
        default=False,
        description="Whether waste is expected during delivery, installation, or commissioning"
    )

    waste_types: List[str] = Field(
        default_factory=list,
        description="Types of waste expected (e.g. packaging, offcuts, hazardous materials)"
    )

    disposal_responsibility: Literal["supplier", "purchaser", "shared", "not_applicable"] = Field(
        default="not_applicable",
        description="Who is responsible for removing or disposing of the waste"
    )

    segregation_required: bool = Field(
        default=False,
        description="Whether waste must be segregated (e.g. recyclable vs hazardous)"
    )

    take_back_or_recycling_policy: str = Field(
        default="",
        description="Purchaser-specific requirements such as take-back schemes or recycling protocols"
    )

    documentation_required: bool = Field(
        default=False,
        description="Whether documentation or reporting on waste type, quantity, or disposal is required"
    )

class S307_Facts(BaseModel):
    section_status: Literal["in_progress", "complete"] = Field(
        default="in_progress",
        description="Completion status for the section"
    )

    qms_required: bool = Field(
        default=False,
        description="Whether the Supplier is required to have a formal Quality Management System"
    )

    requires_iso_9001: bool = Field(
        default=False,
        description="Whether ISO 9001 certification is required"
    )

    other_certifications: List[str] = Field(
        default_factory=list,
        description="Other mandatory QMS certifications or standards (e.g. ISO 13485, AS9100)"
    )

    purchaser_specific_procedures: List[str] = Field(
        default_factory=list,
        description="Purchaser-defined QA/QC procedures, review gates, or reporting formats"
    )

    quality_plan_required: bool = Field(
        default=False,
        description="Whether a project-specific quality plan must be submitted"
    )

    quality_plan_due: Optional[str] = Field(
        default=None,
        description="Deadline or phase when the quality plan must be submitted (e.g. before manufacture)"
    )

    record_retention_required: bool = Field(
        default=False,
        description="Whether the Supplier must retain quality records"
    )

    record_retention_period: Optional[str] = Field(
        default=None,
        description="How long quality records must be retained, if applicable"
    )

    third_party_audit_required: bool = Field(
        default=False,
        description="Whether any part of the QMS must be independently certified or audited"
    )

class ContactPerson(BaseModel):
    full_name: str = Field(..., description="Full name of the contact person")
    role: str = Field(..., description="Job title or functional role (e.g. Delivery Coordinator)")
    responsibility: str = Field(..., description="Area of responsibility (e.g. inspections, logistics, training)")
    email: str = Field(..., description="Email address of the contact person")
    phone_number: str = Field(..., description="Direct phone number for the contact person")

class S308_Facts(BaseModel):
    section_status: Literal["in_progress", "complete"] = Field(
        default="in_progress",
        description="Completion status for the section"
    )

    supplier_contacts: List[ContactPerson] = Field(
        ...,
        description="List of primary Supplier-side contacts relevant to delivery, coordination, or issue resolution"
    )

    purchaser_contacts: List[ContactPerson] = Field(
        ...,
        description="List of primary Purchaser-side contacts relevant to delivery, coordination, or issue resolution"
    )

    escalation_contacts: Optional[List[ContactPerson]] = Field(
        default=None,
        description="Optional list of escalation contacts if primary persons are unavailable"
    )

class CommunicationPlatform(BaseModel):
    name: str = Field(..., description="Name of the system or platform (e.g. SharePoint, Asite, MS Teams)")
    purpose: str = Field(..., description="Purpose of use (e.g. document uploads, status updates, messaging)")
    access_url: Optional[str] = Field(None, description="Link or portal URL if applicable")
    requires_credentials: bool = Field(..., description="Indicates whether login credentials or permissions are needed")
    access_notes: Optional[str] = Field(None, description="Additional instructions or notes for system access")

class SubmissionProtocol(BaseModel):
    applies_to: str = Field(..., description="Type of communication (e.g. reports, drawings, RFIs)")
    file_format: Optional[str] = Field(None, description="Preferred file format (e.g. PDF, DOCX)")
    naming_convention: Optional[str] = Field(None, description="Required naming convention for submitted files")
    version_control_method: Optional[str] = Field(None, description="Versioning requirement or system (e.g. V1, V2, date-based)")

class S309_Facts(BaseModel):
    section_status: Literal["in_progress", "complete"] = Field(
        default="in_progress",
        description="Completion status of the section"
    )

    platforms: List[CommunicationPlatform] = Field(
        ...,
        description="List of systems or tools approved for communication between the Purchaser and Supplier"
    )

    submission_protocols: Optional[List[SubmissionProtocol]] = Field(
        default=None,
        description="Defined rules for submitting files via the communication systems"
    )

    credentials_provided: Optional[bool] = Field(
        default=None,
        description="Indicates whether necessary credentials or access have been confirmed with the Supplier"
    )

class ReportRequirement(BaseModel):
    type: str = Field(..., description="Type of report (e.g. weekly status, monthly dashboard, progress update)")
    frequency: str = Field(..., description="Reporting frequency (e.g. weekly, biweekly, monthly)")
    format: Optional[str] = Field(None, description="Preferred format (e.g. PDF, Excel, Portal Upload)")
    submission_method: Optional[str] = Field(None, description="How the report is submitted (e.g. email, upload to portal)")
    recipients: Optional[List[str]] = Field(None, description="List of recipients who must receive the report")

class MeetingRequirement(BaseModel):
    meeting_type: str = Field(..., description="Type of meeting (e.g. kickoff, weekly progress, monthly review)")
    frequency: str = Field(..., description="How often the meeting occurs (e.g. weekly, monthly)")
    participants: List[str] = Field(..., description="List of required participants by role (e.g. Supplier PM, Purchaser Rep)")
    host_responsibility: Optional[str] = Field(None, description="Who is responsible for hosting or coordinating the meeting")
    minute_taker: Optional[str] = Field(None, description="Who takes minutes or records actions")

class TerminologyConvention(BaseModel):
    term: str = Field(..., description="Defined term or abbreviation used in reports or meetings")
    meaning: str = Field(..., description="What the term or abbreviation means in this project context")

class S310_Facts(BaseModel):
    section_status: Literal["in_progress", "complete"] = Field(
        default="in_progress",
        description="Completion status of the section"
    )

    reports: List[ReportRequirement] = Field(
        ...,
        description="Reporting expectations including types, cadence, formats, and recipients"
    )

    meetings: List[MeetingRequirement] = Field(
        ...,
        description="Planned meetings required during delivery, with roles and cadence"
    )

    terminology_conventions: Optional[List[TerminologyConvention]] = Field(
        default=None,
        description="List of specific terminology, acronyms, or formats the Supplier must follow"
    )

    documentation_templates: Optional[List[str]] = Field(
        default=None,
        description="URLs to templates, dashboards, or reporting formats required for submissions"
    )


class Context(BaseModel):
    next_question: str = Field(default="Start the interview by greeting the user. Ask if they have any background information they would like to share.", description="Next question to ask")
    current_section: SectionID = Field(default=SectionID.S101, description="Current section of the NEC4 SCC contract")
    s101_facts: S101_Facts = Field(default_factory=S101_Facts, description="Purchaser's Objectives")
    s102_facts: S102_Facts = Field(default_factory=S102_Facts, description="Description of the Goods")
    s103_facts: S103_Facts = Field(default_factory=S103_Facts, description="Drawings")