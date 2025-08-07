from typing import List, Optional
from pydantic import BaseModel, Field
from agents.context_management.session_contexts.section_context import SectionContextBase, SectionID
import rich

# -----------------------------
# GLOBAL CONTEXT MODEL
# -----------------------------

class InterviewContext(BaseModel):
    section_id: SectionID = Field(default=SectionID.S101, description="Which section the interview is currently in")
    sections: List[SectionContextBase] = Field(default_factory=list, description="All section contexts containing facts and status")

    def get_section(self, section_id: SectionID) -> Optional[SectionContextBase]:
        return next((s for s in self.sections if s.section_id == section_id), None)

    def get_current_section(self) -> Optional[SectionContextBase]:
        return self.get_section(self.section_id)

    def next_section(self) -> None:
        return ""

    def update_section(self, new_section: SectionContextBase) -> None:
        for idx, section in enumerate(self.sections):
            if section.section_id == new_section.section_id:
                self.sections[idx] = new_section
                return
        raise ValueError(f"Section {new_section.section_id} not found in InterviewContext.")
    
    def print(self):
        rich.print("INTERVIEW CONTEXT: " + self.model_dump_json(indent=1))         

    def print_current_section(self):
        rich.print("CURRENT SECTION: " + self.get_current_section().model_dump_json(indent=1))         
