from typing import List, Optional
from pydantic import BaseModel, Field
from agents.context_management.session_contexts.section_context import SectionContext, SectionID
import rich

# -----------------------------
# GLOBAL CONTEXT MODEL
# -----------------------------

class InterviewContext(BaseModel):
    current_section: SectionID = Field(default=SectionID.S101, description="Which section the interview is currently in")
    sections: List[SectionContext] = Field(default_factory=list, description="All section contexts containing facts and status")

    def get_section(self, section_id: SectionID) -> Optional[SectionContext]:
        return next((s for s in self.sections if s.section == section_id), None)

    def get_current_section(self) -> Optional[SectionContext]:
        return self.get_section(self.current_section)

    def update_section(self, new_section: SectionContext) -> None:
        for idx, section in enumerate(self.sections):
            if section.section == new_section.section:
                self.sections[idx] = new_section
                return
        raise ValueError(f"Section {new_section.section} not found in InterviewContext.")
    
    def print(self):
        rich.print(self.model_dump_json(indent=2))         

    def print_current_section(self):
        rich.print(self.get_current_section().model_dump_json(indent=2))         
