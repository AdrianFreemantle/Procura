from agents.context_management import SectionID 
from agents.agent_prompts import *
from agents.context_management.session_contexts.contexts import *
from typing import Dict
from agents.context_management.session_contexts.contexts import *
from agents.agent_prompts.section_definitions import *

SECTION_DEFINITIONS: Dict[SectionID, str] = {
    SectionID.S101: SECTION_S101_DEFINITION,
    SectionID.S102: SECTION_S102_DEFINITION,
    SectionID.S103: SECTION_S103_DEFINITION,
    SectionID.S104: SECTION_S104_DEFINITION,
    SectionID.S105: SECTION_S105_DEFINITION,
    SectionID.S106: SECTION_S106_DEFINITION,
    SectionID.S107: SECTION_S107_DEFINITION,
    SectionID.S108: SECTION_S108_DEFINITION,
    SectionID.S109: SECTION_S109_DEFINITION,
    SectionID.S110: SECTION_S110_DEFINITION,
    SectionID.S111: SECTION_S111_DEFINITION,
    SectionID.S112: SECTION_S112_DEFINITION,
    SectionID.S201: SECTION_S201_DEFINITION,
    SectionID.S202: SECTION_S202_DEFINITION,
    SectionID.S301: SECTION_S301_DEFINITION,
    # Add more as needed
}

def build_prompt(section_id: SectionID) -> str:
    if section_id not in SECTION_DEFINITIONS:
        raise ValueError(f"Unknown section ID: {section_id}") 

    if(section_id in [SectionID.S102, SectionID.S201]):
        return base_prompts.INTERVIEWER_PROMPT + "\n" + SECTION_DEFINITIONS[section_id] + "\n" + S102_CONTEXT_STRUCTURE;  
    
    return base_prompts.INTERVIEWER_PROMPT + "\n" + SECTION_DEFINITIONS[section_id] + "\n" + FACTS_CONTEXT_STRUCTURE;  