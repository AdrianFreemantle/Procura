from agents.context_management import SectionID 
from agents.agent_prompts import *
from agents.context_management.context import S101_Facts
from enum import Enum

SECTION_DEFINITIONS = {
    "S101": SECTION_S101_DEFINITION,
    "S102": SECTION_S102_DEFINITION,
    "S103": SECTION_S103_DEFINITION,
    # Add more as needed
}

class PromptRole(str, Enum):
    INTERVIEWER = "interviewer"
    FACT_EVALUATOR = "fact_evaluator"    

def generate_schema_block(section_id, model_class):
    lines = [f"FACTS SCHEMA FOR {section_id}", "="*10]
    
    for field_name, field in model_class.model_fields.items():
        if field_name == "section_status":
            continue
        description = field.description.strip().rstrip(".") + "."
        lines.append(f"- `{field_name}`: {description}")
    
    return "\n".join(lines)

def build_prompt(section_id: SectionID, role: PromptRole) -> str:
    section_key = section_id.value if isinstance(section_id, SectionID) else section_id    

    if section_key not in SECTION_DEFINITIONS:
        raise ValueError(f"Unknown section ID: {section_key}") 

    schema_block = generate_schema_block(section_id, S101_Facts)
    
    if role == PromptRole.FACT_EVALUATOR:
        return base_prompts.FACT_EVALUATOR_PROMPT + "\n\n" + schema_block
    
    if role == PromptRole.INTERVIEWER:        
        return base_prompts.INTERVIEWER_PROMPT + "\n\n" + schema_block + "\n\n" + SECTION_DEFINITIONS[section_key]
    
    raise ValueError(f"Unknown role: {role}")