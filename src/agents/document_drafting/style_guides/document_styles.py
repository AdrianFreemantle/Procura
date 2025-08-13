from typing import Dict
from agents.context_management.session_contexts.contexts import SectionID
from pydantic import BaseModel, Field

from agents.agent_prompts.section_definitions import *

class SectionStyleGuide(BaseModel):
    section_id: SectionID = Field(default=SectionID.S101)
    section_name: str = Field(default="")
    purpose: str = Field(default="")
    style_guide: str = Field(default="")
    section_output: str = Field(default="")
    examples: str = Field(default="")
    context_structure: str = Field(default="")

    def system_prompt(self):
        return f"Section Style Guide: {self.style_guide}\nSection Examples: {self.examples}\n"

    def developer_prompt(self):
        return f"Section Output: {self.section_output}\nSection ID: {self.section_id}\nSection Name: {self.section_name}\nSection Purpose: {self.purpose}\nContext Structure: {self.context_structure}\n"    

class DocumentationStyles(BaseModel):
    section_style: Dict[SectionID, SectionStyleGuide] = Field(default_factory=dict)   

DOCUMENTATION_STYLES = DocumentationStyles()

#===================================
# S101
#===================================

S101_PURPOSE = """
- A high-level explanation of why the Purchaser needs the goods
- Helps Supplier understand what the Purchaser is trying to achieve and sets the context for evaluating the suitability of the goods
"""

S101_STYLE_GUIDE = """
Use Markdown syntax for formatting.
Avoid bullet points for this section
Section heading format: H2 `section_id` `section_name`
"""

S101_OUTPUT = """
Provide one or two short paragraphs summarising the Purchaser's objectives.
"""

S101_EXAMPLE = """
H2 S101 Purchaser's Objectives
The objective of the Client is to establish a state-of-the-art Smelting Plant with the capacity to process 18,000 tons per annum of PGM feedstock, employing DC furnace technology. This new plant will replace Arc 4, which is scheduled for decommissioning.

The Client has set specific goals to achieve with this project, including minimising the inherent risks associated with the smelting process, enhancing the recovery of precious group metals (PGM) from the smelting operation, increasing the throughput capacity of the process units, reducing operational costs per ton processed, and improving the accuracy of metal accounting and business reporting for the process units. By pursuing these objectives, the Client aims to optimize efficiency, productivity, and cost-effectiveness in their smelting operations.
"""

DOCUMENTATION_STYLES.section_style[SectionID.S101] = SectionStyleGuide(
    section_id=SectionID.S101,
    section_name="Client's objectives",
    purpose=S101_PURPOSE,  
    style_guide=S101_STYLE_GUIDE,
    examples=S101_EXAMPLE,
    section_output=S101_OUTPUT,
    context_structure=FACTS_CONTEXT_STRUCTURE
)

#===================================
# S102
#===================================

S102_STYLE_GUIDE = """    
Use Markdown syntax for formatting.
Section heading format: H2 `section_id` `section_name`
Each deliverable bullet point starts with the deliverable name in bold, then a colon, then a description of the deliverable.
"""    

S102_PURPOSE = """
- Provide a clear description of the goods to be supplied
- Establish the baseline for what must be delivered and assessed
"""

S102_OUTPUT = """
Begin section with 'The Supplier provides the following deliverables:'
Bullet point list of deliverables
"""

S102_EXAMPLE = """
H2 S102 Description of the Goods
The Supplier provides the following deliverables:
- **The Support Plan:** Plan detailing post-handover support and assistance for addressing any issues or questions.
- **The Alloy Transfer Car:** Complete with geared motor drives, rail scrapers, spring loaded power cable reel, local control panel, radio remote control, rails and rail support beams.
"""

DOCUMENTATION_STYLES.section_style[SectionID.S102] = SectionStyleGuide(
    section_id=SectionID.S102,
    section_name="Description of the Goods",
    purpose=S102_PURPOSE,   
    style_guide=S102_STYLE_GUIDE,
    examples=S102_EXAMPLE,
    section_output=S102_OUTPUT,
    context_structure=S102_CONTEXT_STRUCTURE
)