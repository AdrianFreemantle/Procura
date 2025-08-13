FACTS_CONTEXT_STRUCTURE = """
CONTEXT_STRUCTURE
========================
`context` contains:
- `message_to_user`: your reply
- `section_id`: current section (e.g., "S101")
- `section_status`: "pending", "in_progress", or "complete"
- `facts`: List of fact objects, each with:
-- `data`: name, description, question, answers[], status ("pending"/"answered"/"not_applicable"/"partial")
""" 

SECTION_S101_DEFINITION = """
SECTION 101 INTERVIEW GUIDANCE:
===========
- FOCUS: High-level business drivers, operational pain points, strategic goals, constraints, benefits in improved outcomes.
- AVOID: Quantitative details, manufacturers, models, delivery/payment terms, or specific technical standards.
"""

SECTION_S102_DEFINITION = """
SECTION 102 INTERVIEW GUIDANCE: 
===========
- Never assume what to put in the goods_descriptions based on S101
- Only place goods in the goods_descriptions list if the user explicitly provides them
- Always ask if there are multiple goods to describe
- For each new good, add an item to `goods_descriptions`.
- Avoid:
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
  - `goods_description`: How the purchaser would describe the goods
  - `intended_use`: High-level operational purpose or function of the goods within the Purchaser's operation.
""" 

SECTION_S103_DEFINITION = """
SECTION 103 INTERVIEW GUIDANCE:
===========
- FOCUS:
  - Drawings showing the design, arrangement, or installation of the goods
  - Complete references for each drawing: number, title, and revision level
  - Inclusion of relevant fabrication, installation, and interface drawings
- AVOID:
  - General facility layout drawings unless they directly relate to the goods
  - Missing or ambiguous references (e.g., absent number, title, or revision)
"""

SECTION_S104_DEFINITION = """
SECTION 104 INTERVIEW GUIDANCE:
===========
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
SECTION 105 INTERVIEW GUIDANCE:
===========
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
SECTION 106 INTERVIEW GUIDANCE:
===========
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
SECTION 107 INTERVIEW GUIDANCE:
===========
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
SECTION 108 INTERVIEW GUIDANCE:
===========
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
- FOCUS:
  - Specific activities requiring method statements or risk assessments (e.g., lifting, transport, installation, working at height, confined space)
  - Submission timing for documents and required notice period
  - Approval flow and roles responsible for review and acceptance
  - Required formats, templates, and any Purchaser submission platforms
- AVOID:
  - General safety rules or training requirements; capture these in Sections S108 or S112
"""

SECTION_S110_DEFINITION = """
SECTION 110 INTERVIEW GUIDANCE:
===========
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
SECTION 111 INTERVIEW GUIDANCE:
===========
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
SECTION 112 INTERVIEW GUIDANCE:
===========
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
SECTION 201 INTERVIEW GUIDANCE:
===========
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
SECTION 202 INTERVIEW GUIDANCE:
===========
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
SECTION 301 INTERVIEW GUIDANCE:
===========
- FOCUS:
  - Purchaser-specific rules or site conditions the Supplier must follow
  - Constraints arising from environmental permits or ecological sensitivity
  - Requirements from other stakeholders (e.g., neighbours, authorities) that the Supplier must comply with
  - Clear, concrete constraints (e.g., “no deliveries after 6pm”, “no access to Zone C”)
- AVOID:
  - Technical specifications or material restrictions; capture these in Section S200
"""