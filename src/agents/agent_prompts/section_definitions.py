FACTS_CONTEXT_STRUCTURE = """
CONTEXT_STRUCTURE
========================
The `context` includes:
- `message_to_user`: Your reply to the user is placed here.
- `section_id`: The current section (e.g., "S101")
- `section_status`: "pending", "in_progress", or "complete".
- `facts`: A list of fact objects, each with: 
  - `data`: 
    - `name`: fact name
    - `description`: fact description
    - `question`: Suggested question
    - `answers`: A string array of facts.
    - `status`: "pending", "answered", "not_applicable", or "partial" if more info needed. 
""" 

SECTION_S101_DEFINITION = """
SECTION 101 INTERVIEW GUIDANCE:
===========
- FOCUS:
  - High-level business drivers
  - Operational pain points, strategic goals, constraints
  - Benefits in terms of improved outcomes
- AVOID:
  - Quantitave values: Number of goods, rated capacity, dimensions, weight 
  - Manufacturer, Model, implementation details, delivery methods/schedules, payment terms 
  - Specific technical standards, compliance frameworks, detailed performance criteria
"""

SECTION_S102_DEFINITION = """
SECTION 102 INTERVIEW GUIDANCE: 
===========
- Always ask the user if they have any more goods they want to describe before completing section
- For each goods the Purchaser wants to describe, add a new item to `goods_descriptions`
- AVOID :
  - Vague terms (e.g., "adequate", "typical", "suitable for purpose")
  - Technical standards, detailed performance criteria, or acceptance limits
  - Installation, delivery, handling, packaging, or training details 
  - Quantities or delivery batches 
"""

S102_CONTEXT_STRUCTURE = """
CONTEXT_STRUCTURE
========================
The `context` includes:
- `section_id`: The current section (e.g., "S102")
- `section_status`: "pending", "in_progress", or "complete".
- `message_to_user`: Your reply to the user is placed here.
- `goods_descriptions`: A list of goods descriptions, each with the following fields:
  - `goods_common_name`: The name or designation the Purchaser uses for the goods, used consistently in the contract and related documents.
  - `core_characteristics`: The factual attributes that identify the goods, including type, model, size or dimensions, capacity, and, where relevant, configuration or variant codes.
  - `intended_use`: High-level operational purpose or function of the goods within the Purchaser's operation.
""" 

SECTION_S103_DEFINITION = """
SECTION 103 RULES:
===========
SECTION ID: S103

SECTION TITLE: Drawings

SECTION PURPOSE: 
 - List all drawings, diagrams, or schematics required to define or illustrate the goods
 - Ensure visual documents align with the written description and confirm design intent

NEC4 SSC CLAUSE REFERENCE: 11.2(11)(a)

MANDATORY: false

INTERVIEW GUIDANCE:
- FOCUS:
  - Drawings showing the design, arrangement, or installation of the goods
  - Complete references for each drawing: number, title, and revision level
  - Inclusion of relevant fabrication, installation, and interface drawings
- AVOID:
  - General facility layout drawings unless they directly relate to the goods
  - Missing or ambiguous references (e.g., absent number, title, or revision)
"""

SECTION_S104_DEFINITION = """
SECTION 104 RULES:
===========
SECTION ID: S104

SECTION TITLE: Tests and Inspections

SECTION PURPOSE: 
 - Specify the tests and inspections required to verify the goods meet required quality standards
 - Define who performs the tests, when and where they occur, and the acceptable results to reduce acceptance disputes

NEC4 SSC CLAUSE REFERENCE: 40.1

MANDATORY: false

INTERVIEW GUIDANCE:
- FOCUS:
  - The set of tests or inspections required before acceptance
  - Responsibility, location, and timing for each test or inspection
  - Pass/fail criteria, standards, methods, and tolerances to be applied
  - Required witnesses or sign-off roles
  - Acceptance documentation and certificates to be provided
- AVOID:
  - General safety inspections or Purchaser audits of documentation; those belong in Sections S108 and S111
"""

SECTION_S105_DEFINITION = """
SECTION 105 RULES:
===========
SECTION ID: S105

SECTION TITLE: Samples

SECTION PURPOSE: 
 - Define whether physical samples must be provided before fabrication or delivery
 - Specify submission, review, and acceptance or rejection processes to confirm expectations early

NEC4 SSC CLAUSE REFERENCE: 11.2(11)(a)

MANDATORY: false

INTERVIEW GUIDANCE:
- FOCUS:
  - Whether samples are required prior to manufacturing or delivery
  - The type of samples to be submitted and the acceptance procedure
  - Submission rules for samples: packaging, labelling, and delivery method
  - Who reviews or witnesses the sample and how acceptance is decided
  - Whether any samples are retained and for what purpose
  - Whether the sample represents the final colour, material, or construction standard
- AVOID:
  - Performance testing of samples; those requirements belong under S104 (Tests and Inspections)
"""

SECTION_S106_DEFINITION = """
SECTION 106 RULES:
===========
SECTION ID: S106

SECTION TITLE: Management of Tests and Inspections

SECTION PURPOSE: 
 - Describe how tests and inspections will be organised, coordinated, and recorded
 - Define attendance, access arrangements, required documentation, and result submission so activities run smoothly

NEC4 SSC CLAUSE REFERENCE: 40.1

MANDATORY: false

INTERVIEW GUIDANCE:
- FOCUS:
  - Overall management and coordination plan for tests and inspections
  - Scheduling, notice periods, and sequencing to avoid delays
  - Required records, certificates, and reporting formats
  - Submission process for results, including channels, timing, and recipients
  - Use of Purchaser forms or templates where specified
- AVOID:
  - Test procedures, methods, acceptance values, or performance criteria; these belong in Section S104
"""

SECTION_S107_DEFINITION = """
SECTION 107 RULES:
===========
SECTION ID: S107

SECTION TITLE: Correcting Defects

SECTION PURPOSE: 
 - Outline the process for correcting defects found during testing, inspection, or delivery
 - Define reporting, access arrangements for repairs, and retesting to enable timely, controlled resolution

NEC4 SSC CLAUSE REFERENCE: 11.2(2), 40.1

MANDATORY: true

INTERVIEW GUIDANCE:
- FOCUS:
  - Notification and reporting process when a defect is identified
  - Roles responsible for authorising repair or replacement
  - Access arrangements, coordination, and logistics for rework
  - Retesting and reinspection protocol for corrected items
  - Evidence of correction to be submitted before final acceptance
- AVOID:
  - New test requirements or performance standards; list those in Section S104
"""

SECTION_S108_DEFINITION = """
SECTION 108 RULES:
===========
SECTION ID: S108

SECTION TITLE: Health and Safety Requirements

SECTION PURPOSE: 
 - List Purchaser-specific health and safety requirements beyond legal compliance
 - Align Supplier activities with the Purchaser’s internal safety standards

NEC4 SSC CLAUSE REFERENCE: 11.2(11)(b)

MANDATORY: false

INTERVIEW GUIDANCE:
- FOCUS:
  - Purchaser-specific health and safety procedures and site rules the Supplier must follow
  - Required training, inductions, permits, and safety documentation
  - Reporting protocols for incidents, near misses, and safety performance
  - Site access, supervision requirements, and PPE standards
  - Rules for high-risk activities (e.g., working at height, hot work, confined spaces)
  - Links to Purchaser HSE policies or required documents
- AVOID:
  - Method statements; these belong in Section S109
  - Statutory legal duties; these belong in Section S110
"""

SECTION_S109_DEFINITION = """
SECTION 109 RULES:
===========
SECTION ID: S109

SECTION TITLE: Method Statements

SECTION PURPOSE: 
 - Specify which activities require Supplier method statements or risk assessments for Purchaser review
 - Ensure higher-risk activities are planned safely and reviewed before execution

NEC4 SSC CLAUSE REFERENCE: 11.2(11)(b)

MANDATORY: false

INTERVIEW GUIDANCE:
- FOCUS:
  - Specific activities requiring method statements or risk assessments (e.g., lifting, transport, installation, working at height, confined space)
  - Submission timing for documents and required notice period
  - Approval flow and roles responsible for review and acceptance
  - Required formats, templates, and any Purchaser submission platforms
- AVOID:
  - General safety rules or training requirements; capture these in Sections S108 or S112
"""

SECTION_S110_DEFINITION = """
SECTION 110 RULES:
===========
SECTION ID: S110

SECTION TITLE: Statutory Requirements

SECTION PURPOSE: 
 - Identify legal and regulatory duties that apply to the goods and their supply
 - Ensure the Supplier is aware of approvals, permits, and documentation required beyond the contract

NEC4 SSC CLAUSE REFERENCE: 11.2(11)(b)

MANDATORY: false

INTERVIEW GUIDANCE:
- FOCUS:
  - Applicable national, regional, or industry-specific laws and regulations
  - Required approvals, permits, and licenses before or during supply
  - Named legal dutyholders (e.g., regulators, inspectors, appointed persons) and how the Supplier must engage with them
  - Statutory documentation to be provided or retained and when it is due
- AVOID:
  - Site safety procedures; capture these in Section S108
  - Method statements or risk assessments; capture these in Section S109
"""

SECTION_S111_DEFINITION = """
SECTION 111 RULES:
===========
SECTION ID: S111

SECTION TITLE: Inspections of Safety Procedures

SECTION PURPOSE: 
 - State whether the Purchaser will inspect, review, or audit the Supplier’s safety procedures
 - Define expectations for transparency, documentation, and compliance during the contract

NEC4 SSC CLAUSE REFERENCE: 11.2(11)(b)

MANDATORY: false

INTERVIEW GUIDANCE:
- FOCUS:
  - Whether the Purchaser will conduct inspections or audits of the Supplier’s safety systems and procedures
  - Safety documents to be submitted for review and how they are provided
  - Frequency, timing, and format of inspections or audits (e.g., documentation checks, site visits)
  - Scope of the inspection or audit and assessment criteria
  - The Purchaser role or team responsible for conducting the review
- AVOID:
  - The Supplier’s own safety rules or procedures; capture these in Section S108
  - Method statements or risk assessments; capture these in Section S109
"""

SECTION_S112_DEFINITION = """
SECTION 112 RULES:
===========
SECTION ID: S112

SECTION TITLE: Training Requirements

SECTION PURPOSE: 
 - Detail training or accreditation the Supplier must provide to the Purchaser’s staff
 - Specify when, where, and how training will be delivered for operation, maintenance, or safety

NEC4 SSC CLAUSE REFERENCE: 11.2(11)(b)

MANDATORY: false

INTERVIEW GUIDANCE:
- FOCUS:
  - Whether the Supplier must provide training to the Purchaser’s team
  - Training topics to be covered (operation, safety, maintenance)
  - Timing and location of training, and the number of attendees
  - Delivery method (on-site or remote) and required training materials
  - Qualifications required of the trainer
  - Whether certification or sign-off is required
  - Whether training must be completed before Delivery or Handover
- AVOID:
  - Internal training for the Supplier’s own staff
"""

SECTION_S201_DEFINITION = """
SECTION 201 RULES:
===========
SECTION ID: S201

SECTION TITLE: Specifications

SECTION PURPOSE: 
 - List the technical specifications the Supplier must comply with
 - Organise general, discipline-specific, component-level, or assembly-level criteria so each part of the goods is clearly defined

NEC4 SSC CLAUSE REFERENCE: 11.2(11)(b)

MANDATORY: true

CONTEXT_STRUCTURE
========================
you are given a `context` object in the developer prompt:

At each `context` includes:
- 'grouping_option': ask the user how they want their requirements to be grouped
- `message_to_user`: Your reply to the user is placed here.
- `section_id`: The current section (e.g., "S101")
- `section_status`: "pending", "in_progress", or "complete".
- `specfication_items`: A list of specificationsections, each with: 
  - `subject`: What is being specified(e.g., General requirements, Operation and control requirements, Safety requirements, Mud Gun requirements, Drills requirements).
  - `requirements`: A free form list of bullet point statements that describe the requirement e.g. 
    - Examples:   
      - 'The mud guns are remotely operable and controllable from a safe distance.'
      - 'The control system allows precise adjustment of flow rates to optimise taphole sealing operations.'
      - 'The equipment undergoes rigorous factory testing and acceptance procedures to ensure compliance with specifications before delivery.'
    
INTERVIEW GUIDANCE:
- When an answer provided by the user contains more than 1 requirement, split them into separate 'requirements' entries.
- Examples of the type of information captured in requirements:
  - General requirements: baseline expectations that apply to all equipment.
  - Compliance and standards: named standards, codes, statutory duties.
  - Materials and construction: material suitability, corrosion resistance, build quality.
  - Dimensions and capacity: size envelope, load, throughput, clearances.
  - Operating conditions: temperature, pressure, vibration, hot splash, environment.
  - Interfaces and compatibility: fit with existing plant, control systems, utilities.
  - Operation and control: modes, adjustability, setpoints, local vs remote control.
  - Safety features: guards, interlocks, E-stops, alarms.
  - Quality assurance and verification: factory tests, acceptance before delivery, inspections.
  - Documentation and labelling: manuals, labels, handling instructions.
  - Packaging and transport: protection for transit and storage.
  - Maintainability and access: ease of maintenance, service access, replaceable parts.
- DO NOT ASK FOR:
  - Exact models, types and quantities
  - Describing what the goods are; capture this in Section S102
  - Including test procedures; capture these in Section S104
  - Vague terms (e.g., "adequate", "typical", "suitable for purpose")
  - Quantities or delivery batches 
"""

SECTION_S202_DEFINITION = """
SECTION 202 RULES:
===========
SECTION ID: S202

SECTION TITLE: Deleterious and Hazardous Materials

SECTION PURPOSE: 
 - List materials the Supplier is not allowed to use
 - Support safety, environmental compliance, and alignment with Purchaser policies

NEC4 SSC CLAUSE REFERENCE: 11.2(11)(b)

MANDATORY: false

INTERVIEW GUIDANCE:
- FOCUS:
  - Banned or restricted materials, hazardous substances, chemicals, insulation types, and coatings
  - Legal or environmental regulations that limit material choices
  - Purchaser-specific policies, sustainability rules, and client blacklists
  - Upload and reference applicable standards or policy documents
  - Explicit confirmation if no restrictions apply
- AVOID:
  - General health and safety procedures; capture these in Section S108
"""

SECTION_S301_DEFINITION = """
SECTION 301 RULES:
===========
SECTION ID: S301

SECTION TITLE: General Constraints

SECTION PURPOSE: 
 - State general restrictions on how the Supplier performs their work
 - Make the Supplier aware of non-negotiable boundaries arising from legal, environmental, community, or Purchaser policies

NEC4 SSC CLAUSE REFERENCE: 11.2(11)(b)

MANDATORY: false

INTERVIEW GUIDANCE:
- FOCUS:
  - Purchaser-specific rules or site conditions the Supplier must follow
  - Constraints arising from environmental permits or ecological sensitivity
  - Requirements from other stakeholders (e.g., neighbours, authorities) that the Supplier must comply with
  - Clear, concrete constraints (e.g., “no deliveries after 6pm”, “no access to Zone C”)
- AVOID:
  - Technical specifications or material restrictions; capture these in Section S200
"""