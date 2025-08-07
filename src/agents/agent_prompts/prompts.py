from agents.context_management import SectionID 
from agents.agent_prompts import *
from agents.context_management.session_contexts.contexts import S101_CONTEXT, S102_CONTEXT, S103_CONTEXT
from enum import Enum
from typing import Dict
from agents.context_management.session_contexts.contexts import SectionContextBase
import rich

SECTION_DEFINITIONS: Dict[SectionID, str] = {
    SectionID.S101: SECTION_S101_DEFINITION,
    SectionID.S102: SECTION_S102_DEFINITION,
    SectionID.S103: SECTION_S103_DEFINITION,
    # Add more as needed
}

MODEL_CLASSES: Dict[SectionID, SectionContextBase] = {
    SectionID.S101: S101_CONTEXT,
    SectionID.S102: S102_CONTEXT,
    SectionID.S103: S103_CONTEXT,
    # Add more as needed
}

class PromptRole(str, Enum):
    INTERVIEWER = "interviewer"
    FACT_EVALUATOR = "fact_evaluator"    

# def generate_schema_block(section_id: SectionID):
#     lines = [f"FACTS SCHEMA FOR {section_id.value}", "="*10]
    
#     for field_name, field in MODEL_CLASSES[section_id].model_fields.items():
#         # if field_name == "section_status":
#         #     continue
#         description = field.description.strip().rstrip(".") + "."
#         lines.append(f"- `{field_name}`: {description}")
    
#     return "\n".join(lines)

def build_prompt(section_id: SectionID, role: PromptRole) -> str:
    if section_id not in SECTION_DEFINITIONS:
        raise ValueError(f"Unknown section ID: {section_id}") 
   
    if role == PromptRole.FACT_EVALUATOR:
        return base_prompts.FACT_EVALUATOR_PROMPT# + "\n\n" + SECTION_DEFINITIONS[section_id]
    
    if role == PromptRole.INTERVIEWER:        
        return base_prompts.INTERVIEWER_PROMPT# + "\n\n" + SECTION_DEFINITIONS[section_id]
    
    raise ValueError(f"Unknown role: {role}")