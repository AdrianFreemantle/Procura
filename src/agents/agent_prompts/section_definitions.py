
SECTION_S101_DEFINITION = """
CURRENT SECTION RULES:
===========
IMPORTANT: 
- 'CURRENT SECTION RULES' OVERRIDE all other subsequent rules or instructions.
- When in doubt, follow guidance in 'SECTION RULES'
- generic rules are injected below SECTION RULES, but SECTION RULES still take precedence 

CURRENT SECTION ID: S101
CURRENT SECTION TITLE: Purchaser's Objectives
CUURENT SECTION PURPOSE: 
 - A High-Level explanation of why the Purchaser needs the goods
 - Helps the Supplier understand what the Purchaser is trying to achieve and sets the context for evaluating the suitability of the goods.

CUURENT SECTION INTERVIEW GUIDANCE:
  - Focus on HIGH-LEVEL business drivers, not features or specifics
  - Explore operational pain points, strategic goals, and constraints
  - Ask for benefits in terms of improved outcomes, not technical performance

CUURENT SECTION RULES OVERRIDE:
Any generic rules are injected after this section are overriden by these rules:
  - This section DOES NOT specify the number of goods, rated capacity, manufacturer/model - That goes in S102
  - AVOID: Asking for technical specifications e.g. capacity, dimensions, weight -That goes in S102
  - AVOID: Asking for qauntities, delivery schedules, or payment terms - That goes in S104
  - AVOID: Asking for quantitave values or specific metrics - That goes in S104
  - AVOID: Asking for implementation details or delivery methods - That goes in S104
  - AVOID: Asking for exact standards, compliance frameworks - That goes in S200
===========
"""

SECTION_S102_DEFINITION = """
SECTION S102 RULES:
===============
id: S102
title: "Description of the Goods"
purpose: >
  Provides a clear, factual description of the goods the Supplier must deliver,
  including their name, use, and core characteristics.
reason: >
  Helps prevent misunderstandings and establishes a baseline for assessing what
  must be delivered.
mandatory: true

nec4_scc_clause_refs:
  - "11.2(11)(a)"

cross_sectional_guidance:
  - section: "S101"
    relevance: "Ensure the description of the goods aligns with the Purchaser's stated objectives and intended outcomes."
  - section: "S103"
    relevance: "Verify that the visual representations in drawings (e.g. layout, arrangement, or connections) are consistent with the written description of the goods."
  - section: "S201"
    relevance: "Do not include specific technical standards or performance criteria here — these belong in Section S201 (Specifications) and should be referenced only as needed for clarity."

depends_on_sections:
  - "S101"

interview_guidance:
  - "Ask what the goods are called or referred to as by the Purchaser."
  - "Clarify what the goods will be used for in the Purchaser’s operation."
  - "Capture measurable attributes like type, model, size, or capacity."
  - "Avoid vague or subjective descriptors — aim for objective facts."
  - "If brand or origin is important, confirm whether it's a preference or a constraint."
  - "Note if optional variants or accessories are expected."

out_of_scope_topics:
  - "Detailed technical specifications or standards (belongs in S200-series)."
  - "Functional performance benchmarks (handled later in testing/acceptance sections)."
  - "Installation or integration details (belongs in method statements or works information)."

completion_rules:
  - "All fact fields in S102 Context are marked as N/A or have a valid valu

"""

SECTION_S103_DEFINITION = """
SECTION S103 RULES:
===============
id: S103
title: "Drawings"
purpose: "Lists all drawings, diagrams, or schematics that are required to help define or illustrate the goods."
reason: >
  Ensures that the visual documents match the written descriptions and can be used by the Supplier to confirm design intent.
mandatory: conditional
nec4_scc_clause_refs:
  - "11.2(11)(a)"
related_sections:
  - "S102"
  - "S500"
  - "S600"
cross_sectional_guidance:
  - section: "S102"
    relevance: "Confirm that the drawings visually match the written description of the goods to prevent inconsistencies."
  - section: "S500"
    relevance: "Exclude general layout or coordination drawings of the overall facility unless they directly relate to the goods being supplied."
  - section: "S600"
    relevance: "General works coordination drawings should be placed in Section S600, not in S103, unless directly tied to the goods."
interview_guidance:
  - "Ask if there are drawings that show how the goods are designed, arranged, or installed."
  - "Request drawing numbers, titles, and revision levels to ensure accuracy."
  - "Confirm that listed drawings directly relate to the goods and not to unrelated works or facilities."
  - "Encourage inclusion of fabrication, installation, or interface drawings where applicable."
out_of_scope_topics:
  - "General layout drawings of the whole facility unless they directly relate to the goods"
  - "Drawings not referenced in Section S102 or unrelated to the goods"
completion_rules:
  - "Drawing references include number, title, and revision where available"
  - "PURCHASER confirms that all relevant drawings have been listed"
  - "PURCHASER confirms that listed drawings are accurate and applicable to the goods"

"""

SECTION_S104_DEFINITION = """
SECTION S104 RULES:
===============
id: S104
title: "Tests and Inspections"
purpose: "Specifies any tests or inspections required to verify that the goods meet the required quality standards."
reason: >
  Clarifies what tests are needed, who performs them, when and where they occur, and what results are acceptable.
  This reduces the risk of disputes during delivery or acceptance.
mandatory: conditional
nec4_scc_clause_refs:
  - "40.1"
related_sections:
  - "S108"
  - "S111"
cross_sectional_guidance:
  - section: "S108"
    relevance: "Exclude general safety inspections which are handled under health and safety provisions in S108."
  - section: "S111"
    relevance: "Audits or reviews of documentation belong in S111, not in this section unless they are part of formal test witnessing."
interview_guidance:
  - "Ask what tests or inspections are required before the goods are accepted."
  - "Clarify who performs the tests, where they will take place, and when they are scheduled."
  - "Confirm any standards, tolerances, or specific test methods that must be followed."
  - "Request pass/fail criteria or acceptance thresholds if available."
  - "Ask if any documentation (e.g. certificates, reports) must be submitted following tests."
out_of_scope_topics:
  - "General safety inspections not tied to the specific goods"
  - "Purchaser audits or administrative reviews of test documentation"
  - "Ongoing operational monitoring or inspections unrelated to initial acceptance"
completion_rules:
  - "PURCHASER confirms whether any tests or inspections are required for the goods"
  - "If applicable, details of tests include who performs them, when and where, and the criteria for acceptance"
  - "PURCHASER confirms whether documentation (e.g. test reports or certificates) must be submitted"
"""

SECTION_S105_DEFINITION = """
SECTION S105 RULES:
===============
id: S105
title: "Samples"
purpose: "Outlines whether the Supplier must provide physical samples of the goods for review or acceptance before full supply or fabrication."
reason: >
  Enables the Purchaser to confirm that the goods meet expectations before production or delivery begins,
  and ensures both parties understand the submission and approval process.
mandatory: conditional
nec4_scc_clause_refs:
  - "11.2(11)(a)"
related_sections:
  - "S104"
cross_sectional_guidance:
  - section: "S104"
    relevance: "Do not include performance testing of samples; those requirements should be captured under S104 (Tests and Inspections)."
interview_guidance:
  - "Ask whether any physical samples of goods are required before manufacturing or delivery."
  - "Clarify what type of samples must be submitted and how acceptance will be determined."
  - "Ask whether there are any requirements for packaging, labelling, or delivery of the samples."
  - "Check if the sample will be retained and whether it sets the standard for final goods (e.g. colour, material, or construction)."
out_of_scope_topics:
  - "Performance testing of samples — handled in S104"
  - "Samples unrelated to visual, tactile, or material quality of the goods"
  - "General QA procedures not involving physical samples"
completion_rules:
  - "PURCHASER confirms whether samples are required"
  - "If required, type of sample, review criteria, and submission instructions are captured"
  - "PURCHASER confirms if any sample will be retained as the benchmark for final goods"

"""

SECTION_S106_DEFINITION = """
SECTION S106 RULES:
===============
id: S106
title: "Management of Tests and Inspections"
purpose: >
  Describes how all tests and inspections will be organised, coordinated, and recorded,
  including presence requirements, access arrangements, documentation, and result submission.
reason: >
  Ensures that tests and inspections are carried out smoothly, without causing delays or confusion.
mandatory: conditional
nec4_scc_clause_refs:
  - "40.1"
related_sections:
  - "S104"
cross_sectional_guidance:
  - section: "S104"
    relevance: "Do not repeat test procedures or acceptance values here — those belong in S104. This section focuses only on management and coordination."
interview_guidance:
  - "Ask how tests and inspections will be managed in terms of planning and logistics."
  - "Clarify who must attend, who approves the results, and how those results are documented."
  - "Request information about timing, access to facilities, and reporting expectations."
  - "Ask if there are any required forms, templates, or sign-off procedures."
out_of_scope_topics:
  - "Describing test procedures or performance standards — belongs in S104"
  - "General QA processes unrelated to tests or inspections"
  - "Equipment specifications used in tests"
completion_rules:
  - "Roles and responsibilities for test and inspection oversight are clearly defined"
  - "PURCHASER has specified access, documentation, and approval protocols"
  - "Any required records, certificates, or templates have been listed"
"""

SECTION_S107_DEFINITION = """
SECTION S107 RULES:
===============
id: S107
title: "Correcting Defects"
purpose: >
  Outlines the process for correcting any defects found during testing, inspection, or delivery,
  including how issues are reported, access for repairs, and how the defect is retested.
reason: >
  Ensures that defective goods are addressed in a controlled and timely way, reducing delays and disputes.
mandatory: conditional
nec4_scc_clause_refs:
  - "11.2(2)"
  - "40.1"
related_sections:
  - "S104"
  - "S105"
cross_sectional_guidance:
  - section: "S104"
    relevance: "New test requirements or acceptance standards should be defined in S104, not here."
  - section: "S105"
    relevance: "If defects relate to submitted samples, cross-reference acceptance criteria and review processes in S105."
interview_guidance:
  - "Ask what process is followed if defects are discovered during inspection or delivery."
  - "Clarify how access for rework or correction will be coordinated."
  - "Ask who is responsible for approving corrective actions or repairs."
  - "Request how the Supplier should demonstrate the defect has been corrected (e.g., reinspection, certificates)."
out_of_scope_topics:
  - "Defining new test criteria or standards — these belong in S104"
  - "Listing general QA policies unrelated to specific defect correction"
  - "Discussing product warranties or commercial remedies — these belong in the contract, not Scope"
completion_rules:
  - "Notification process for reporting defects is clearly defined"
  - "Roles and responsibilities for corrective action are specified"
  - "Reinspection or evidence requirements for corrected goods are documented"
"""

SECTION_S108_DEFINITION = """
SECTION S108 RULES:
===============
id: S108
title: "Health and Safety Requirements"
purpose: >
  Lists any Purchaser-specific health and safety requirements that go beyond general legal compliance.
  This may include safety procedures, reporting protocols, supervision requirements, or rules for
  working on the Purchaser’s site.
reason: >
  Ensures that the Supplier’s work is aligned with the Purchaser’s internal safety standards.
mandatory: conditional
nec4_scc_clause_refs:
  - "11.2(11)(b)"
related_sections:
  - "S109"
  - "S110"
cross_sectional_guidance:
  - section: "S109"
    relevance: "Do not include method statements — these belong in S109."
  - section: "S110"
    relevance: "Legal safety duties or statutory obligations should be defined under S110."
interview_guidance:
  - "Ask whether there are any Purchaser-specific HSE rules beyond statutory obligations."
  - "Ask about PPE standards, site access protocols, or specific safety procedures required by the Purchaser."
  - "Prompt for incident or near-miss reporting requirements and frequency."
  - "Request any training, certifications, or permits the Supplier must hold."
  - "Ask if the Purchaser has formal HSE documentation to be provided or referenced."
out_of_scope_topics:
  - "Method statements — these belong in S109"
  - "General legal safety duties — these belong in S110"
  - "Contractual remedies for safety violations — not part of Scope"
completion_rules:
  - "Site-specific HSE requirements (beyond legal minimum) are clearly described"
  - "Relevant documentation or Purchaser safety policies are referenced or uploaded"
  - "All special conditions for Supplier personnel (e.g., inductions, supervision, PPE) are captured"

"""

SECTION_S109_DEFINITION = """
SECTION S109 RULES:
===============
id: S109
title: "Method Statements"
purpose: >
  Specifies which activities require the Supplier to submit method statements or risk assessments for
  Purchaser review. These are usually linked to higher-risk tasks such as lifting, transport, or installation.
reason: >
  Ensures that these activities are planned safely and reviewed before execution.
mandatory: conditional
nec4_scc_clause_refs:
  - "11.2(11)(b)"
related_sections:
  - "S108"
  - "S112"
cross_sectional_guidance:
  - section: "S108"
    relevance: "Do not duplicate general safety rules or requirements — capture those under S108."
  - section: "S112"
    relevance: "Training requirements should be recorded in S112, not in method statement descriptions."
interview_guidance:
  - "Ask which activities require method statements or risk assessments (e.g., lifting, confined space, hot work)."
  - "Ask when these documents must be submitted (e.g., number of days before work begins)."
  - "Ask who is responsible for reviewing and approving them on the Purchaser side."
  - "Ask whether there are specific templates, formats, or content requirements."
  - "Prompt for reference to Purchaser safety procedures or approval workflows if applicable."
out_of_scope_topics:
  - "General safety rules — these belong in S108"
  - "Training or qualification requirements — these belong in S112"
  - "Legal obligations — covered under statutory duties, not Scope"
completion_rules:
  - "High-risk activities requiring method statements are clearly listed"
  - "Submission timing and approval process is defined"
  - "Document format or templates (if any) are identified"
  - "Links to relevant Purchaser procedures or expectations are included"
"""

SECTION_S110_DEFINITION = """
SECTION S110 RULES:
===============
id: S110
title: "Statutory Requirements"
purpose: >
  Identifies any legal or regulatory duties that apply to the goods or their supply. This may include compliance 
  with national laws, industry-specific regulations, or named dutyholders that must be involved.
reason: >
  Ensures that the Supplier is aware of all legal obligations beyond the contract itself.
mandatory: conditional
nec4_scc_clause_refs:
  - "11.2(11)(b)"
related_sections:
  - "S108"
  - "S109"
cross_sectional_guidance:
  - section: "S108"
    relevance: "Site-specific safety procedures must be recorded in S108, not under statutory requirements."
  - section: "S109"
    relevance: "Method statements and risk assessments are handled in S109; do not duplicate them here."
interview_guidance:
  - "Ask whether there are any legal requirements that apply to the goods or their delivery."
  - "Ask if specific industry or country regulations apply (e.g. hazardous materials, CE marking, etc.)."
  - "Ask if named legal dutyholders must be consulted, informed, or approved (e.g. inspectors, regulators)."
  - "Prompt for documentation, permits, or notices required by law before or during supply."
out_of_scope_topics:
  - "Site safety procedures — those belong in S108"
  - "Method statements or risk assessments — those belong in S109"
  - "Internal Purchaser policies that are not legal obligations"
completion_rules:
  - "Relevant legal and regulatory requirements are listed or confirmed as not applicable"
  - "Dutyholder roles and responsibilities (if any) are clearly described"
  - "Necessary approvals, permits, or statutory documentation are identified"
  - "Any jurisdiction-specific considerations are addressed (e.g. local laws, compliance bodies)"
"""

SECTION_S111_DEFINITION = """
SECTION S111 RULES:
===============
id: S111
title: "Inspections of Safety Procedures"
purpose: >
  States whether the Purchaser will inspect, review, or audit the Supplier’s safety procedures.
reason: >
  Helps define expectations around transparency, documentation, and compliance, and supports the Purchaser in 
  managing safety risk throughout the contract.
mandatory: conditional
nec4_scc_clause_refs:
  - "11.2(11)(b)"
related_sections:
  - "S108"
  - "S109"
cross_sectional_guidance:
  - section: "S108"
    relevance: "Purchaser-defined safety procedures are specified in S108. Do not repeat them here."
  - section: "S109"
    relevance: "Supplier’s method statements are addressed in S109. S111 is limited to Purchaser inspections or audits."
interview_guidance:
  - "Ask whether the Purchaser intends to audit or inspect the Supplier’s safety procedures during the contract."
  - "Ask what safety documents the Supplier must submit for inspection or audit."
  - "Ask how often the inspections will happen and in what format (e.g. site visit, document check)."
  - "Confirm who on the Purchaser’s team is responsible for conducting the inspection or review."
out_of_scope_topics:
  - "The Supplier’s own safety procedures — these belong in S108"
  - "Method statements and risk assessments — covered in S109"
  - "Routine compliance with general law — addressed in S110"
completion_rules:
  - "The Purchaser’s intent to inspect or audit Supplier safety procedures is confirmed or marked not applicable"
  - "Inspection frequency, scope, and required documentation are clearly described"
  - "Responsible Purchaser personnel or roles are identified"

"""

SECTION_S112_DEFINITION = """
SECTION S112 RULES:
===============
id: S112
title: "Training Requirements"
purpose: >
  Details any training or accreditation that the Supplier must provide to the Purchaser’s staff.
reason: >
  Ensures that the Purchaser’s staff are equipped to operate, maintain, or safely use the goods once delivered.
mandatory: conditional
nec4_scc_clause_refs:
  - "11.2(11)(b)"
related_sections:
  - "S101"
  - "S104"
  - "S105"
cross_sectional_guidance:
  - section: "S101"
    relevance: "Training should align with the Purchaser’s stated objectives and intended use of the goods."
  - section: "S104"
    relevance: "If testing or inspection is part of acceptance, training may need to address quality or performance verification."
  - section: "S105"
    relevance: "Training may reference approved samples as a standard for use or handling procedures."
interview_guidance:
  - "Ask whether the Supplier must provide training to the Purchaser’s personnel."
  - "Ask what specific topics the training should cover, such as operation, maintenance, or safety procedures."
  - "Ask when and where the training must take place, and how many staff will attend."
  - "Ask whether training must be completed before delivery, handover, or use."
  - "Ask about requirements for training materials, instructor qualifications, and any certification or sign-off."
out_of_scope_topics:
  - "Internal training for the Supplier’s own personnel"
  - "General onboarding or induction processes unrelated to use of the goods"
  - "Legal or regulatory training — those belong in S110"
completion_rules:
  - "Training requirement is clearly confirmed or marked not applicable"
  - "Scope, timing, and location of training are defined"
  - "Target audience, delivery method, and completion criteria are described"
"""

SECTION_S201_DEFINITION = """
SECTION S201 RULES:
===============
id: S201
title: "Specifications (Expandable)"
purpose: >
  Lists the technical specifications the Supplier must comply with. This includes general requirements as well as discipline-specific, component-level, or assembly-level criteria.
reason: >
  Ensures that each part of the goods is clearly and accurately defined, avoiding ambiguity and providing the Supplier with the technical detail necessary for compliance.
mandatory: true
nec4_scc_clause_refs:
  - "11.2(11)(b)"
related_sections:
  - "S102"
  - "S104"
cross_sectional_guidance:
  - section: "S102"
    relevance: "Specifications must align with the description of the goods to avoid conflict or duplication."
  - section: "S104"
    relevance: "Do not include test procedures or acceptance criteria — those should be defined in the Tests and Inspections section."
interview_guidance:
  - "Begin by confirming how the specifications should be grouped: general, discipline-specific, component-level, or system/assembly-based."
  - "Ask for overall general specifications that apply across all goods (e.g. standards, coatings, materials, finishes)."
  - "Prompt for specific technical details per discipline or component, using subsection headings where appropriate."
  - "Encourage upload or reference of specification documents, datasheets, or standards where available."
  - "Clarify that this section defines what the goods *must comply with* — not how they are described or used."
out_of_scope_topics:
  - "Functional descriptions or use cases of the goods — those belong in S102"
  - "Inspection, testing, or quality procedures — those belong in S104"
  - "Supplier work methods or controls — those belong in S109"
completion_rules:
  - "All applicable subsections are completed or marked as not applicable"
  - "Specifications are structured, either inline or via attached documents, and clearly grouped"
  - "Any referenced documents or uploads are correctly named and tagged"
"""

SECTION_S202_DEFINITION = """
SECTION S202 RULES:
===============
id: S202
title: "Deleterious and Hazardous Materials"
purpose: >
  Lists any materials the Supplier is not allowed to use. This may include banned chemicals, hazardous substances, or materials restricted by law or Purchaser policy.
reason: >
  Helps ensure safety, environmental compliance, and alignment with internal standards, preventing the use of harmful or non-compliant materials.
mandatory: false
nec4_scc_clause_refs:
  - "11.2(11)(b)"
related_sections:
  - "S108"
  - "S110"
cross_sectional_guidance:
  - section: "S108"
    relevance: "Do not include general health and safety procedures here — those should be captured under Health and Safety Requirements (S108)."
  - section: "S110"
    relevance: "If material restrictions are based on statutory regulation, consider referencing them under Statutory Requirements (S110) as well."
interview_guidance:
  - "Ask whether any specific materials, substances, or components are prohibited from use in the goods."
  - "Prompt for examples such as asbestos, lead-based paints, certain insulation types, or VOC-heavy coatings."
  - "Ask whether the Purchaser has internal blacklists or sustainability standards that apply."
  - "Allow the user to upload or reference policy documents, client restrictions, or environmental compliance lists."
  - "If no restrictions apply, confirm this explicitly and note as 'N/A' to avoid assumptions later."
out_of_scope_topics:
  - "General site safety procedures — include those in S108"
  - "Statutory legal duties — those should be listed in S110"
completion_rules:
  - "All known material restrictions are listed or the field is marked 'N/A'"
  - "Any uploads or referenced lists are correctly named and accessible"
  - "User confirms there are no additional material restrictions beyond what is captured"
"""

SECTION_S301_DEFINITION = """
SECTION S301 RULES:
===============
id: S301
title: "General Constraints"
purpose: >
  States any general restrictions on how the Supplier performs their work. This includes limitations arising from legal, environmental, community, or internal Purchaser policies.
reason: >
  Ensures the Supplier is aware of non-negotiable boundaries governing how goods are supplied, helping to prevent non-compliance, conflict, or project delays.
mandatory: false
nec4_scc_clause_refs:
  - "11.2(11)(b)"
related_sections:
  - "S200"
  - "S401"
cross_sectional_guidance:
  - section: "S200"
    relevance: "Do not include technical specifications here — those should be listed under Specifications (S200)."
  - section: "S401"
    relevance: "Programme-related constraints (e.g. access times or sequencing) may also be reflected in the Delivery Programme (S401). Coordinate with that section to ensure consistency."
interview_guidance:
  - "Ask whether the Purchaser has internal policies or community expectations that limit how or when work is done."
  - "Prompt for environmental constraints such as noise limits, restricted working hours, or protection zones."
  - "Ask if any legal obligations or permits require specific conduct (e.g. heritage protection, road usage)."
  - "Check if neighbouring properties, tenants, or authorities impose operational restrictions on the Supplier."
  - "Request examples in plain language, such as 'no deliveries before 7am' or 'Supplier must avoid using access road B'."
out_of_scope_topics:
  - "Technical performance requirements or material restrictions — covered in S200"
  - "Detailed delivery timelines — those belong in S401"
  - "Method statements — those are covered in S109"
completion_rules:
  - "All relevant general constraints are listed or the field is explicitly marked 'N/A'"
  - "Constraints are stated clearly in a way the Supplier can interpret and comply with"
  - "The Purchaser confirms all listed constraints are complete and accurate"
"""

SECTION_S303_DEFINITION = """
SECTION S302 RULES:
===============
id: S302
title: "Confidentiality"
purpose: >
  Specifies any confidentiality obligations the Supplier must comply with during or after the contract. This may include handling of sensitive technical data, proprietary information, or public communications.
reason: >
  Protects the Purchaser’s commercial information, intellectual property, and public reputation by clearly defining what must remain confidential and under what conditions.
mandatory: false
nec4_scc_clause_refs:
  - "11.2(11)(b)"
related_sections:
  - "Contract Data"
  - "S303"
cross_sectional_guidance:
  - section: "Contract Data"
    relevance: "Do not duplicate general contract-wide confidentiality terms — refer to Contract Data or core Conditions if already defined."
  - section: "S303"
    relevance: "If specific documents are confidential, also reflect this in the Document Submission and Approval section (S303)."
interview_guidance:
  - "Ask whether the Purchaser requires the Supplier to keep certain technical, commercial, or site-specific information confidential."
  - "Prompt for restrictions on publicity, media engagement, or social media during or after the contract."
  - "Ask whether any Subcontractors must sign NDAs or be bound by similar confidentiality requirements."
  - "Inquire about restrictions on site photography, use of drawings for other work, or retention of technical files after the project."
out_of_scope_topics:
  - "General contract-wide confidentiality obligations — these are handled in Contract Data"
  - "IP ownership clauses — refer to legal terms or conditions of contract"
  - "Document control procedures — see S303 for approval and submission workflows"
completion_rules:
  - "All specific confidentiality obligations are listed or section marked 'N/A'"
  - "The scope, duration, and parties affected by confidentiality terms are clearly stated"
  - "Purchaser confirms all restrictions are necessary and correctly described"
"""

SECTION_S303_DEFINITION = """
SECTION S303 RULES:
===============
id: S303
title: "Security and Identification of People"
purpose: >
  Outlines security rules for people working at or visiting the Purchaser’s premises. This may include vetting, induction, access permits, or ID badge requirements.
reason: >
  Ensures that only approved and authorised personnel access the Purchaser’s facilities, protecting sensitive areas and maintaining operational safety and security.
mandatory: false
nec4_scc_clause_refs:
  - "11.2(11)(b)"
related_sections:
  - "S108"
  - "S304"
cross_sectional_guidance:
  - section: "S108"
    relevance: "Do not include general safety procedures or PPE requirements here — those belong in S108 (Health and Safety Requirements)."
  - section: "S304"
    relevance: "If document handling or site entry depends on identification, reflect these rules in S304 (Document Submission and Approval)."
interview_guidance:
  - "Ask whether Supplier personnel require security clearance, background checks, or special approval before site access is granted."
  - "Prompt for site-specific induction or training that must be completed prior to access."
  - "Ask about access control rules, such as ID badges, biometric systems, visitor lists, or escorts for non-cleared personnel."
  - "Confirm if there are restrictions on time-of-day access, duration of presence, or movement between zones."
out_of_scope_topics:
  - "PPE, safety training, or general health and safety protocols — these are covered in S108"
  - "Document control or digital access permissions — covered under S304"
  - "Confidentiality obligations — see S302"
completion_rules:
  - "All mandatory access rules and identification procedures are captured or marked 'N/A'"
  - "Induction or clearance process is clearly described if required"
  - "Purchaser confirms site-specific security expectations are complete and correct"
"""

SECTION_S304_DEFINITION = """
SECTION S304 RULES:
===============
id: S304
title: "Protection of the Goods"
purpose: >
  Defines how the Supplier must protect the goods during handling, storage, or transport prior to delivery.
reason: >
  Ensures that goods are not damaged, tampered with, or exposed to unsafe conditions before delivery, maintaining integrity and compliance with contractual requirements.
mandatory: false
nec4_scc_clause_refs:
  - "11.2(11)(b)"
related_sections:
  - "S102"
  - "S600"
cross_sectional_guidance:
  - section: "S102"
    relevance: "Protection measures must be suitable for the type, size, and material of goods described in S102."
  - section: "S600"
    relevance: "Do not include delivery responsibilities or logistics — those are defined in S600 (Delivery and Access)."
interview_guidance:
  - "Ask what measures must be taken to prevent damage to the goods during handling or interim storage."
  - "Prompt for protection against environmental exposure, such as rain, humidity, dust, or temperature fluctuations."
  - "Ask whether any specific packaging, wrapping, crating, or tagging methods are required."
  - "Clarify if protection must remain in place until installation or inspection is complete."
  - "Inquire about protective measures on-site, such as fencing, covers, or vibration dampening."
out_of_scope_topics:
  - "Delivery responsibilities or logistics (timing, route, access) — covered in S600"
  - "Inspection procedures or criteria — covered in S104"
  - "General site constraints or rules — covered in S301"
completion_rules:
  - "All specified protection measures are documented or explicitly marked as N/A"
  - "Purchaser confirms that protective requirements are clear and sufficient for contract compliance"
"""

SECTION_S305_DEFINITION = """
SECTION S305 RULES:
===============
id: S305
title: "Industrial Relations"
purpose: >
  States any rules or expectations about how the Supplier interacts with labour representatives, trade unions, or site-based personnel.
reason: >
  Helps prevent disruption due to labour disputes or misunderstandings and ensures smooth coordination with on-site labour or community expectations.
mandatory: false
nec4_scc_clause_refs:
  - "11.2(11)(b)"
related_sections:
  - "S301"
  - "S600"
cross_sectional_guidance:
  - section: "S301"
    relevance: "Site-specific behavioural constraints, such as labour protocols or community hiring rules, may also be captured in S301 (General Constraints)."
  - section: "S600"
    relevance: "Labour coordination during delivery or installation may overlap with access protocols defined in S600."
interview_guidance:
  - "Ask if the Supplier must comply with any union, labour, or industrial relations policies specific to the Purchaser or site."
  - "Inquire whether there are any agreements with trade unions or site-based contractors the Supplier must be aware of."
  - "Prompt for community expectations or local hiring policies that might influence workforce planning."
  - "Ask if there are known sensitivities related to subcontractor engagement or labour disputes on similar past projects."
  - "Clarify if the Supplier must attend site induction or industrial relations briefings."
out_of_scope_topics:
  - "Employment contract terms or worker remuneration — outside project scope"
  - "Safety procedures or method statements — captured in S108 and S109"
  - "Delivery or installation sequencing — covered in S600"
completion_rules:
  - "All known industrial relations obligations are listed, referenced, or explicitly marked as N/A"
  - "Purchaser confirms the Supplier is aware of any local or site-specific expectations regarding workforce behaviour or union coordination"
"""

SECTION_S306_DEFINITION = """
SECTION S306 RULES:
===============
id: S306
title: "Waste Management"
purpose: >
  Describes how the Supplier must manage and dispose of waste produced while delivering the goods.
reason: >
  Ensures that waste is handled safely, responsibly, and in compliance with legal, environmental, or Purchaser-specific requirements.
mandatory: false
nec4_scc_clause_refs:
  - "11.2(11)(b)"
related_sections:
  - "S200"
  - "S301"
cross_sectional_guidance:
  - section: "S200"
    relevance: "Waste arising from materials or components specified in S200 may be subject to environmental or disposal constraints captured here."
  - section: "S301"
    relevance: "General site restrictions, such as local bylaws or environmental permits in S301, may influence how waste is stored or removed."
interview_guidance:
  - "Ask whether the Supplier will generate waste (e.g. packaging, offcuts, consumables) during delivery, installation, or commissioning."
  - "Prompt for disposal responsibilities: Is the Supplier required to remove waste from site or use the Purchaser's systems?"
  - "Inquire about requirements for segregation (e.g. recyclable vs hazardous waste) or use of labelled skips or bins."
  - "Ask if the Purchaser enforces take-back schemes, landfill bans, or has preferred recycling methods."
  - "Clarify if documentation or reporting on waste quantities, type, or disposal method is required."
out_of_scope_topics:
  - "Design specifications for environmental performance — covered in S200"
  - "Constraints unrelated to waste (e.g. delivery routes, noise limits) — covered in S301"
completion_rules:
  - "Waste generation scenarios have been discussed and marked as N/A or with defined obligations"
  - "Purchaser confirms that all responsibilities for removal, recycling, or reporting have been clearly stated or referenced"
"""

SECTION_S307_DEFINITION = """
SECTION S307 RULES:
===============
id: S307
title: "Quality Management System"
purpose: >
  Defines what quality management systems the Supplier must follow, including accreditation, internal controls, and documentation of compliance.
reason: >
  Ensures that quality control is maintained consistently throughout the supply process, supporting traceability and alignment with Purchaser expectations.
mandatory: false
nec4_scc_clause_refs:
  - "11.2(11)(b)"
related_sections:
  - "S104"
  - "S106"
  - "S107"
cross_sectional_guidance:
  - section: "S104"
    relevance: "S104 covers individual test and inspection requirements; S307 should describe the overarching system and quality framework within which those tests are managed."
  - section: "S106"
    relevance: "S106 covers the logistics of managing inspections; S307 addresses the formal systems or certifications used to govern quality."
  - section: "S107"
    relevance: "If defects are found, the corrective process in S107 may need to align with documented procedures in the Supplier’s QMS described here."
interview_guidance:
  - "Ask if the Supplier must be accredited to a recognised quality standard (e.g. ISO 9001)."
  - "Inquire about any Purchaser-mandated procedures, reporting formats, or control points for quality assurance."
  - "Check if a project-specific quality plan is required, and when it must be submitted."
  - "Ask if there is a requirement to retain quality records, and for how long."
  - "Ask whether any aspects of the Supplier's system require third-party certification or audit."
out_of_scope_topics:
  - "Detailed inspection activities — captured in S104"
  - "Inspection coordination and access — covered in S106"
  - "Corrective actions or rework procedures — covered in S107"
completion_rules:
  - "Purchaser has confirmed whether a QMS is required and if ISO certification is mandatory"
  - "Any Purchaser-specific quality documentation, review points, or reporting requirements are clearly listed or uploaded"
  - "Quality plan requirements, if applicable, have been specified or marked as N/A"
"""

SECTION_S308_DEFINITION = """
SECTION S308 RULES:
===============
id: S308
title: "Contact Details"
purpose: >
  Lists the key contact people on both sides of the contract, including roles, responsibilities, and communication details.
reason: >
  Ensures communication, coordination, and issue resolution are directed to the correct individuals during supply and delivery, avoiding delays or miscommunication.
mandatory: true
nec4_scc_clause_refs:
  - "11.2(11)(b)"
related_sections:
  - "S106"
  - "S112"
cross_sectional_guidance:
  - section: "S106"
    relevance: "Coordination of tests and inspections often depends on having clear contact roles — contact details here support the logistics described in S106."
  - section: "S112"
    relevance: "Training delivery and planning requires coordination between technical and administrative contacts — contact info here helps enable those interactions."
interview_guidance:
  - "Ask for the name, title, phone number, and email of the Supplier's main contact for delivery coordination."
  - "Ask for the Purchaser’s representative responsible for overseeing delivery or resolving issues."
  - "Ask whether there are different contacts for technical issues, site access, documentation, or logistics."
  - "Request any escalation contacts if the primary individuals are unavailable."
  - "Clarify that legal or contract negotiation contacts are excluded from this section."
out_of_scope_topics:
  - "Legal or contractual representatives for claims or disputes"
  - "Historical correspondence records"
  - "Contact persons unrelated to delivery or coordination"
completion_rules:
  - "At least one named contact is recorded for both Supplier and Purchaser, with full name, title, email, and phone number"
  - "Roles and responsibilities (e.g. delivery lead, technical rep, documentation manager) are clearly identified"
  - "Contact records are complete and verified for accuracy"
"""

SECTION_S309_DEFINITION = """
SECTION S309 RULES:
===============
id: S309
title: "Communication System"
purpose: >
  Describes the tools or systems that must be used for exchanging information between the Purchaser and Supplier.
reason: >
  Ensures smooth, traceable, and standardised communication throughout the contract by defining acceptable platforms and protocols.
mandatory: false
nec4_scc_clause_refs:
  - "11.2(11)(b)"
related_sections:
  - "S308"
  - "S310"
cross_sectional_guidance:
  - section: "S308"
    relevance: "Defined contacts in S308 must align with the communication channels listed here to ensure messages are directed to the correct recipients."
  - section: "S310"
    relevance: "Communication systems specified here must support the reporting and documentation flows described in S310 — avoid duplication or conflicting systems."
interview_guidance:
  - "Ask what system the Supplier must use to send documents, updates, or correspondence (e.g. email, SharePoint, Asite, MS Teams)."
  - "Ask if there is a preferred file format (e.g. PDF, DOCX), naming convention, or versioning rule."
  - "Ask whether there is a centralised location to upload reports or log queries."
  - "Ask if login credentials or user permissions must be arranged in advance."
  - "Clarify that this section covers communication tools only, not the content or frequency of reporting."
out_of_scope_topics:
  - "Document content, performance reports, or KPIs (covered in S310)"
  - "Legal correspondence or contractual notices (covered in the Conditions of Contract)"
  - "Internal Purchaser systems not accessible to the Supplier"
completion_rules:
  - "All required communication platforms or systems are named and their access methods described"
  - "Any submission protocols (e.g. file naming, upload location, permissions) are recorded or linked"
  - "Supplier has confirmed access or has been provided the necessary links or credentials"
"""

SECTION_S310_DEFINITION = """
SECTION S310 RULES:
===============
id: S310
title: "Management Procedures"
purpose: >
  Outlines the day-to-day procedures the Supplier must follow for managing delivery. This may include meetings, reporting, terminology, or formats.
reason: >
  Ensures that both parties have shared expectations for how the supply process will be run, supporting coordination, transparency, and consistent communication.
mandatory: false
nec4_scc_clause_refs:
  - "11.2(11)(b)"
related_sections:
  - "S308"
  - "S309"
cross_sectional_guidance:
  - section: "S308"
    relevance: "Contact roles in S308 should be reflected in the attendance and responsibilities defined in this section’s meeting and reporting procedures."
  - section: "S309"
    relevance: "Submission methods and communication tools used to transmit reports and meeting outputs should align with the systems specified in S309."
interview_guidance:
  - "Ask what reports the Supplier must submit (e.g. weekly status, progress updates, dashboards)."
  - "Ask how frequently these reports are required and in what format (e.g. PDF, Excel, portal upload)."
  - "Ask what meetings are required (e.g. weekly progress, monthly review), who must attend, and who is responsible for hosting or minute-taking."
  - "Ask whether specific terminology, file structures, or abbreviations must be followed."
  - "Clarify that this section is limited to operational management and not contract-wide governance or dispute resolution procedures."
out_of_scope_topics:
  - "Governance frameworks or board-level reviews — these belong in the Conditions of Contract or external governance documentation"
  - "Reporting on legal or financial compliance — unless directly linked to day-to-day delivery tracking"
  - "Contractual notices or formal correspondence (covered in Conditions of Contract)"
completion_rules:
  - "All required meeting types and cadences are defined"
  - "Reporting expectations are documented, including frequency, recipients, and formats"
  - "Any required templates, dashboards, or terminology conventions are listed or referenced"
  - "Responsibility for hosting, submitting, and archiving reports and minutes is assigned"
"""

SECTION_S311_DEFINITION = """
SECTION S311 RULES:
===============
id: S311
title: "Supplier’s Invoice Requirements"
purpose: >
  States what information the Supplier must include on their invoices. This may include item breakdowns, references, contact details, or evidence of delivery.
reason: >
  Ensures that invoices can be processed without delay or rejection by aligning with the Purchaser’s administrative and verification processes.
mandatory: true
nec4_scc_clause_refs:
  - "11.2(11)(b)"
related_sections:
  - "S308"
  - "S600"
cross_sectional_guidance:
  - section: "S308"
    relevance: "Ensure contact roles in S308 include those responsible for receiving, verifying, or querying invoices."
  - section: "S600"
    relevance: "Reference delivery documentation or sign-off evidence from S600 if required to accompany invoices."
interview_guidance:
  - "Ask what must be included on the invoice (e.g. purchase order number, line items, quantities, unit costs)."
  - "Ask if there is a required format, file type, or submission template for invoices."
  - "Ask if proof of delivery, inspection certificates, or other supporting documentation must accompany the invoice."
  - "Ask who the invoice should be addressed to and where it must be sent (email, portal, physical address)."
  - "Clarify that this section excludes payment terms, due dates, or invoicing frequency — those belong in the Contract Data or Conditions of Contract."
out_of_scope_topics:
  - "Payment terms, due dates, or invoicing schedule — covered in the Conditions of Contract"
  - "Banking details or tax registration requirements — unless explicitly required by the Purchaser’s invoice format"
  - "General commercial terms — handled in the contract, not the Scope"
completion_rules:
  - "Invoice content requirements are listed, including all mandatory fields"
  - "Any required format or template is referenced or uploaded"
  - "Supporting documentation expectations (e.g. proof of delivery) are defined"
  - "Recipient contact information and submission method is clearly stated"

"""

SECTION_S312_DEFINITION = """
SECTION S312 RULES:
===============
id: S312
title: "Restrictions or Requirements for Subcontracting"
purpose: >
  Lists any restrictions or conditions the Supplier must meet when using subcontractors. This may include approval procedures, scope limitations, or obligations to disclose who is involved.
reason: >
  Ensures the Purchaser retains oversight of who is delivering key parts of the goods and mitigates delivery, legal, or reputational risks arising from subcontracting.
mandatory: false
nec4_scc_clause_refs:
  - "11.2(11)(b)"
related_sections:
  - "S308"
  - "S307"
cross_sectional_guidance:
  - section: "S308"
    relevance: "Ensure contact details include those responsible for approving or coordinating with subcontractors."
  - section: "S307"
    relevance: "If subcontractors are involved in quality-critical work, confirm their QMS compliance under S307."
interview_guidance:
  - "Ask whether the Supplier is permitted to use subcontractors at all, and if so, for which parts of the work."
  - "Ask whether prior written approval from the Purchaser is required before engaging any subcontractor."
  - "Ask whether the Purchaser maintains a list of pre-approved or prohibited subcontractors."
  - "Ask whether the Supplier must submit information about subcontractors (e.g. company name, scope of work, qualifications) for review."
  - "Clarify that this section does not include technical specifications for subcontracted work — those go in S200."
out_of_scope_topics:
  - "Technical or performance requirements for subcontracted work — covered in S200"
  - "Payment terms between the Supplier and subcontractor — not within Purchaser scope"
  - "Contractual terms or legal agreements between Supplier and subcontractor — unless required for Purchaser approval"
completion_rules:
  - "Clear statement of whether subcontracting is allowed and under what conditions"
  - "Approval thresholds or procedures are defined (e.g. value, scope, or type of work)"
  - "List of required documentation for subcontractor vetting is included"
  - "Any known approved or prohibited subcontractors are referenced, if applicable"

"""

SECTION_S313_DEFINITION = """
SECTION S313 RULES:
===============
id: S313
title: "Marking of Goods"
purpose: >
  Describes how the Supplier must mark goods before they are delivered. This could include labelling, serial numbers, tags, or packaging identification.
reason: >
  Ensures traceability, correct receipt, and smooth handover by allowing the Purchaser and Supplier to verify the identity and status of goods at all stages of delivery.
mandatory: false
nec4_scc_clause_refs:
  - "71.1"
related_sections:
  - "S600"
  - "S102"
cross_sectional_guidance:
  - section: "S600"
    relevance: "Marking should align with any packing or delivery documentation requirements in the Delivery and Transport section."
  - section: "S102"
    relevance: "Goods described in S102 must be clearly identifiable by the markings specified here."
interview_guidance:
  - "Ask whether goods must be marked, tagged, or labelled before delivery to support traceability or asset management."
  - "Ask what format the markings must take (e.g. barcodes, QR codes, stamped plates, printed stickers)."
  - "Ask where the markings should be located on the goods or packaging."
  - "Ask what information must be included in the markings (e.g. asset ID, part number, serial number, batch number)."
  - "Ask whether any standard templates, fonts, or colours must be used."
  - "Clarify that packing instructions belong in S600 and not in this section."
out_of_scope_topics:
  - "Packing, shipping, or crating instructions — covered in S600"
  - "Functional labelling of controls or interfaces — if applicable, that belongs in specifications under S201"
  - "Safety signage or warning labels — typically part of HSE or specification documents"
completion_rules:
  - "Marking requirements are clearly described, including what needs to be marked and how"
  - "Marking content (e.g. serial number, QR code, product ID) is specified or linked to Purchaser standards"
  - "Physical method of marking is included (e.g. riveted plate, adhesive tag)"
  - "Location of markings on the product or packaging is stated"
"""

SECTION_S401_DEFINITION = """
SECTION S401 RULES:
===============
id: S401
title: "Programme Requirements"
purpose: >
  States whether the Supplier is required to submit a programme and what that programme must contain, including format, timing, and level of detail.
reason: >
  A clear programme supports planning, progress monitoring, and proactive management of delivery risks by aligning expectations between the Supplier and Purchaser.
mandatory: false
nec4_scc_clause_refs:
  - "31.1"
related_sections:
  - "S310"
  - "S600"
cross_sectional_guidance:
  - section: "S310"
    relevance: "Programme requirements should align with meeting and reporting expectations defined in Management Procedures."
  - section: "S600"
    relevance: "Programme should consider logistics, delivery dates, and any lead time expectations detailed in Delivery and Transport."
interview_guidance:
  - "Ask if the Supplier is required to submit a programme or schedule for the delivery or manufacture of the goods."
  - "Ask what format the programme should take (e.g. Gantt chart, milestone plan, list of activities)."
  - "Ask whether a specific software tool (e.g. Microsoft Project, Primavera P6, Excel) must be used for compatibility with Purchaser systems."
  - "Ask what level of detail is expected (e.g. high-level tasks only, or detailed per component/system)."
  - "Ask if updates are required during delivery, and how frequently they must be submitted."
  - "Ask if both electronic and printed formats are required and whether sign-off is needed."
out_of_scope_topics:
  - "Detailed descriptions of individual activities or work methods — those belong in S310 or S109"
  - "Day-to-day management procedures — these are covered in S310"
  - "Physical delivery logistics — these belong in S600"
completion_rules:
  - "It is clear whether a programme is required or not"
  - "The expected format and software (if any) are specified"
  - "The level of detail required in the programme is stated"
  - "Submission timing and frequency (e.g. initial and updates) are included"
  - "Method of submission (electronic, hard copy) and review/approval process is described"

"""

SECTION_S402_DEFINITION = """
SECTION S402 RULES:
===============
id: S402
title: "Programme Content"
purpose: >
  Defines what information must be shown on the programme, including milestones, dependencies, testing, approvals, and Purchaser activities.
reason: >
  Ensures the programme serves as an effective coordination tool by clearly identifying obligations, dates, and sequencing relevant to the delivery of goods.
mandatory: false
nec4_scc_clause_refs:
  - "31.1"
related_sections:
  - "S104"
  - "S106"
  - "S310"
  - "S600"
cross_sectional_guidance:
  - section: "S104"
    relevance: "Test periods and sequencing from S104 should appear on the programme to plan quality assurance activities."
  - section: "S106"
    relevance: "Witnessing and inspection management events from S106 must be coordinated on the programme."
  - section: "S310"
    relevance: "Any recurring meetings or management events from S310 may be included for planning clarity."
  - section: "S600"
    relevance: "Delivery dates and transport milestones from S600 should be reflected as key programme events."
interview_guidance:
  - "Ask what key activities or delivery milestones must be shown on the programme."
  - "Ask if Purchaser responsibilities (e.g. approvals, drawing reviews, inspections) must be included as separate events."
  - "Ask if test periods, approvals, or hold points need to be shown with start/end dates."
  - "Ask if responsibilities for each activity should be identified (e.g. Supplier, Purchaser, Shared)."
  - "Ask if the programme must show float, critical path, or lead times."
  - "Ask if internal deadlines (prior to delivery) must be captured (e.g. factory acceptance testing, documentation submission)."
out_of_scope_topics:
  - "High-level submission requirements — those belong in S401"
  - "Daily management processes — these are covered in S310"
  - "Transport arrangements and logistics — covered in S600"
completion_rules:
  - "Key milestones and activities affecting delivery are included"
  - "Purchaser responsibilities (if any) are clearly listed"
  - "Testing, inspection, and approval windows are included"
  - "Responsibilities for each activity are assigned"
  - "Format expectations like float or critical path visibility are addressed"
"""

SECTION_S403_DEFINITION = """
SECTION S403 RULES:
===============
id: S403
title: "Submitting and Updating the Programme"
purpose: >
  Specifies when the Supplier must submit the initial programme, how frequently updates are required, and what those updates must include. This section provides the framework for maintaining visibility over delivery progress and managing deviations.
reason: >
  Helps maintain alignment between Purchaser and Supplier throughout the delivery period by establishing clear rules for programme submission, update frequency, and the handling of delays or changes.
mandatory: false
nec4_scc_clause_refs:
  - "31.1"
related_sections:
  - "S401"
  - "S402"
  - "S310"
cross_sectional_guidance:
  - section: "S401"
    relevance: "Initial submission format and baseline requirements from S401 influence the expectations set in this section."
  - section: "S402"
    relevance: "Changes to programme content may require revised versions under S403 to reflect updated milestones or dependencies."
  - section: "S310"
    relevance: "Programme updates may feed into status meetings and progress reporting obligations defined in S310."
interview_guidance:
  - "Ask when the initial programme must be submitted (e.g. within X days of contract award)."
  - "Ask how often the programme must be updated (e.g. fortnightly, monthly, upon deviation)."
  - "Ask what each updated programme must include (e.g. actual vs planned progress, delay causes, mitigation steps)."
  - "Ask who must approve revised programmes and whether comments are formally tracked."
  - "Ask if resubmission is required for specific triggers (e.g. delay > 5 days, rejection of prior programme, major change)."
out_of_scope_topics:
  - "Document formatting or submission platforms — handled in S310 or S309"
  - "Meeting content or frequencies — addressed in S310"
completion_rules:
  - "Initial submission timing is specified"
  - "Update frequency is defined"
  - "Triggers for resubmission are clear"
  - "Content of revised programmes is outlined"
  - "Approval or review process is defined"
"""

SECTION_S404_DEFINITION = """
SECTION S404 RULES:
===============
id: S404
title: "Delivery Requirements"
purpose: >
  Summarises the work that must be completed by the Delivery Date and identifies the physical delivery location. It ensures both parties know when and where the goods must be delivered and what completion looks like.
reason: >
  Prevents ambiguity about when delivery is achieved and where goods must arrive. Supports planning, logistics, and coordination with related site or project activities.
mandatory: true
nec4_scc_clause_refs:
  - "11.2(4)"
  - "31.1"
related_sections:
  - "S104"
  - "S403"
  - "S601"
cross_sectional_guidance:
  - section: "S104"
    relevance: "Tests that must be completed before or after delivery affect how delivery is defined and confirmed."
  - section: "S403"
    relevance: "The delivery milestone must appear in the programme and any updates if timing changes."
  - section: "S601"
    relevance: "The delivery address and any handling instructions must be consistent with transport arrangements in S601."
interview_guidance:
  - "Ask what the contractual Delivery Date is and whether it applies to supply only, or also to testing, installation, or commissioning."
  - "Ask where the goods must be delivered — site, Purchaser’s warehouse, port of entry, or other specified location."
  - "Ask whether the delivery can be phased or must be completed in a single consignment."
  - "Ask what constitutes 'delivered' — arrival at site, completion of handover, or post-test acceptance."
  - "Ask for a full delivery address, including any reference to specific zones, buildings, or personnel."
out_of_scope_topics:
  - "Incoterms, insurance, or customs documentation — handled in S600"
  - "Transport packaging or marking — covered in S313 and S600"
completion_rules:
  - "Delivery Date is clearly specified"
  - "Delivery location is fully defined"
  - "Scope of delivery completion is described"
  - "Conditions for partial delivery or acceptance are clarified"
"""

SECTION_S501_DEFINITION = """
SECTION S501 RULES:
===============
id: S501
title: "Services and Other Support Provided by the Purchaser"
purpose: >
  Lists any services, facilities, utilities, equipment, or access arrangements the Purchaser must provide to support the supply of goods. This ensures both parties are clear on dependencies, reduces delivery delays, and assigns responsibilities fairly.
reason: >
  Clarifies what the Supplier can rely on during delivery, helping to coordinate site interfaces, prevent delays, and avoid compensation events due to missing support.
mandatory: conditional
nec4_scc_clause_refs:
  - "16.2"
  - "60.1(5)"
related_sections:
  - "S102"
  - "S404"
  - "S600"
cross_sectional_guidance:
  - section: "S102"
    relevance: "If the Purchaser provides free-issued materials, those must be listed in the Description of the Goods, not here."
  - section: "S404"
    relevance: "Delivery activities may rely on Purchaser support, such as cranes or offloading equipment, especially at site."
  - section: "S600"
    relevance: "Logistics arrangements must account for availability of Purchaser-provided services or facilities."
interview_guidance:
  - "Ask whether the Purchaser will provide utilities such as power, water, or compressed air for use during delivery or installation."
  - "Ask if any on-site facilities (e.g. storage space, workshops, clean rooms) are made available to the Supplier."
  - "Ask whether the Purchaser will assist with offloading, transport, lifting, or positioning of goods."
  - "Ask about times and conditions of access, any advance notice periods, and who is responsible for coordination."
  - "Ask whether Purchaser support is free-issued or chargeable, and whether third-party approvals (e.g. site security) are needed."
out_of_scope_topics:
  - "Materials provided as part of the goods — covered in S102"
  - "Standard contract-wide obligations — covered in main Conditions"
completion_rules:
  - "Purchaser support is clearly defined"
  - "Access conditions or constraints are listed"
  - "Responsibilities for scheduling and coordination are stated"
  - "Any commercial terms (e.g. free-issued vs. chargeable) are clarified"
"""

SECTION_S601_DEFINITION = """
SECTION S601 RULES:
===============
id: S601
title: "Requirements for the Supply"
purpose: >
  Describes any constraints on how the Supplier stores, prepares, or stages the goods before delivery. It includes security, staging, packaging, or internal handling requirements. This ensures that goods are ready, secure, and identifiable before reaching the Purchaser.
reason: >
  Helps the Supplier plan internal logistics and ensures goods are protected, traceable, and compliant with Purchaser requirements before dispatch.
mandatory: conditional
nec4_scc_clause_refs:
  - "11.2(11)(b)"
related_sections:
  - "S313"
  - "S404"
  - "S304"
cross_sectional_guidance:
  - section: "S313"
    relevance: "Marking and ID requirements (e.g. labels, barcodes) must be listed in S313, not here."
  - section: "S404"
    relevance: "Supply preparation must align with final Delivery Date and destination constraints listed in S404."
  - section: "S304"
    relevance: "Requirements for protection of goods during delivery or storage overlap with pre-dispatch staging and should be consistent."
interview_guidance:
  - "Ask if the Supplier must store the goods under specific conditions (e.g. indoors, on pallets, climate control)."
  - "Ask if sealing, security measures, or packaging must be applied before delivery."
  - "Ask whether a final inspection, photographic evidence, or checklists are required before dispatch."
  - "Ask about any hold points or QA steps that must be completed before the goods leave the Supplier’s premises."
  - "Ask if there are instructions on how goods must be staged or grouped prior to transport (e.g. batch-based, asset sets)."
out_of_scope_topics:
  - "Marking, ID, or labelling — covered in S313"
  - "Physical delivery logistics — covered in S604"
completion_rules:
  - "All pre-dispatch storage, protection, and staging requirements are listed"
  - "Final QA or inspection actions (if any) are clearly stated"
  - "Security, climate, or packaging constraints (if applicable) are defined"

"""

SECTION_S602_DEFINITION = """
SECTION S602 RULES:
===============
id: S602
title: "Requirements for Transport"
purpose: >
  Specifies how the goods must be transported, including mode of transport, packaging, handling precautions, and any limitations. It ensures that goods are delivered safely, on time, and in good condition.
reason: >
  Allows the Supplier to plan compliant, secure, and damage-free shipment that meets the Purchaser’s logistical and quality expectations.
mandatory: conditional
nec4_scc_clause_refs:
  - "22.2"
  - "70.1"
related_sections:
  - "S601"
  - "S603"
  - "S605"
  - "S304"
cross_sectional_guidance:
  - section: "S601"
    relevance: "Storage and staging requirements before dispatch must be consistent with transport constraints listed here."
  - section: "S603"
    relevance: "Transport method must align with the Purchaser’s handover location and acceptance procedures in S603."
  - section: "S605"
    relevance: "Transport documentation requirements should not be duplicated here — refer to S605 instead."
  - section: "S304"
    relevance: "Goods protection during transport must complement on-site protection rules listed in S304."
interview_guidance:
  - "Ask what mode(s) of transport are allowed or preferred (e.g. road, rail, sea, air)."
  - "Ask whether the goods have specific packaging, bracing, or tie-down requirements."
  - "Ask if there are height, weight, or clearance limits (e.g. low bridges, narrow gates)."
  - "Ask whether the Purchaser must approve the transport plan, method, or route."
  - "Ask if any escort, permit, or special logistical coordination is needed."
out_of_scope_topics:
  - "Delivery location and handover requirements — covered in S603"
  - "Transport documentation and records — covered in S605"
completion_rules:
  - "Transport mode and constraints (if any) are clearly defined"
  - "Packaging or bracing instructions are included where relevant"
  - "Any Purchaser approvals or special transport arrangements are listed"
"""

SECTION_S603_DEFINITION = """
SECTION S603 RULES:
===============
id: S603
title: "Delivery Place"
purpose: >
  States the precise location where the goods must be delivered. This includes physical address, access constraints, operating hours, and contact details. It ensures successful and timely handover.
reason: >
  Enables the Supplier to plan transport, scheduling, and access arrangements to meet contractual delivery obligations without delay or dispute.
mandatory: yes
nec4_scc_clause_refs:
  - "70.1"
  - "70.2"
related_sections:
  - "S404"
  - "S602"
  - "S605"
  - "S501"
cross_sectional_guidance:
  - section: "S404"
    relevance: "The physical delivery location must match the scope defined as complete at the Delivery Date."
  - section: "S602"
    relevance: "Transport mode and constraints must be compatible with the delivery site's access rules."
  - section: "S605"
    relevance: "Handover procedures and documentation should align with the contact and access details listed here."
  - section: "S501"
    relevance: "If Purchaser-provided services (e.g. cranes, unloading) are needed at delivery, cross-check with S501."
interview_guidance:
  - "Ask for the full delivery address, including any site-specific identifiers (e.g. Gate 3, Warehouse B)."
  - "Ask what days and hours deliveries are accepted."
  - "Ask if there are access constraints (e.g. low bridge, weight limits, escort needed)."
  - "Ask who the Supplier must contact to arrange delivery, and how much notice is required."
  - "Ask if the Purchaser provides offloading equipment or if the Supplier must bring their own."
out_of_scope_topics:
  - "Transport method and packaging — covered in S602"
  - "Delivery documentation or handover process — covered in S605"
completion_rules:
  - "Exact delivery location is clearly defined"
  - "Access rules, timing, and points of contact are provided"
  - "Offloading arrangements and pre-notification rules are included if applicable"

"""

SECTION_S605_DEFINITION = """
SECTION S605 RULES:
===============
id: S605
title: "Information to Be Provided by the Supplier (Domestic Procurement)"
purpose: >
  Lists the documents the Supplier must provide for domestic delivery. This includes delivery notes, packing lists, invoices, and certificates. It ensures the Purchaser can verify receipt and process payment.
reason: >
  Ensures that goods are properly documented upon delivery, supporting verification, traceability, and payment processing. Avoids disputes over incomplete or missing delivery paperwork.
mandatory: yes
nec4_scc_clause_refs:
  - "11.2(11)(b)"
related_sections:
  - "S311"
  - "S603"
  - "S606"
cross_sectional_guidance:
  - section: "S311"
    relevance: "Invoice content defined in S311 must match the documentation issued at delivery under S605."
  - section: "S603"
    relevance: "Delivery location and personnel listed in S603 must align with the recipients of the documents listed here."
  - section: "S606"
    relevance: "If international supply is involved, cross-reference with S606 to separate domestic and cross-border document obligations."
interview_guidance:
  - "Ask what documents must accompany the goods on delivery (e.g. delivery notes, packing lists, test certificates, warranty cards)."
  - "Ask what specific information each document must include (e.g. PO number, part number, batch/serial numbers, descriptions)."
  - "Ask in what format each document must be supplied (e.g. PDF, printed original, barcoded label, scanned copy)."
  - "Ask how many copies are required and who must receive them (e.g. on-site rep, document control, accounts)."
  - "Ask if a standard template or format must be used or submitted in advance for approval."
  - "Ask if electronic copies must be uploaded to a portal, emailed, or physically submitted."
out_of_scope_topics:
  - "Customs declarations or international freight documentation — covered in S606"
  - "Payment terms, invoice due dates, or currencies — covered in S311 and the Contract Data"
completion_rules:
  - "All required document types are explicitly listed"
  - "Each document type includes required data fields"
  - "Submission format (e.g. PDF, hard copy) and number of copies are defined"
  - "Any template requirements or approval steps are documented"
"""

SECTION_S606_DEFINITION = """
SECTION S606 RULES:
===============
id: S606
title: "Information to Be Provided by the Supplier (International Procurement)"
purpose: >
  Describes all import/export documentation required when the goods cross borders. This may include licences, bills of lading, customs declarations, and tax certificates. It ensures that the shipment can move legally and smoothly between countries.
reason: >
  Ensures that international shipments are not delayed, rejected, or penalised due to incomplete or non-compliant documentation. Clarifies cross-border responsibilities between Purchaser and Supplier.
mandatory: if_applicable
nec4_scc_clause_refs:
  - "70.2"
related_sections:
  - "S604"
  - "S605"
  - "S602"
cross_sectional_guidance:
  - section: "S604"
    relevance: "Incoterms and international role-splitting defined in S604 must match the documentation responsibilities in S606."
  - section: "S605"
    relevance: "Domestic delivery documentation (S605) must be separated from international documentation in S606 to avoid duplication or conflict."
  - section: "S602"
    relevance: "Transport arrangements in S602 should reference any carrier documents (e.g. air waybill) listed here."
interview_guidance:
  - "Ask whether the goods cross international borders and require export/import clearance."
  - "Ask what documents must be supplied (e.g. commercial invoice, packing list, bill of lading, certificate of origin, export licence)."
  - "Ask whether the Purchaser or Supplier is responsible for customs clearance and who their customs broker is."
  - "Ask what data must appear on documents (e.g. HS codes, country of origin, net/gross weights)."
  - "Ask if any approvals, authorisations, or compliance certificates (e.g. CE marking, SABS) must accompany the shipment."
  - "Ask about the required format (digital vs. hard copy), language, number of copies, and timing of submission."
out_of_scope_topics:
  - "Domestic-only delivery documents — covered in S605"
  - "Transport method or packaging — covered in S602"
  - "Responsibility split for international supply — covered in S604"
completion_rules:
  - "Section is only completed if cross-border delivery applies"
  - "Each required document type is listed with purpose and responsible party"
  - "Submission method, language, and format are stated"
  - "References to Incoterms or customs agents are included if applicable"
"""

