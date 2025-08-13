from typing import List, Optional
from pydantic import BaseModel, Field
from agents.context_management.session_contexts.section_context import *
from datetime import datetime
# -----------------------------
# GLOBAL CONTEXT MODEL
# -----------------------------

class InterviewContext(BaseModel):
    context_id: Optional[int] = Field(default=None, description="Unique identifier for the interview context")
    context_name: str = Field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"), description="Name of the interview context")
    context_status: str = Field(default="empty", description="Status of the context: empty, active, archived")
    section_id: SectionID = Field(default=SectionID.S101, description="Which section the interview is currently in")
    main_contexts: List[MainContext] = Field(default_factory=list, description="Main context containing all sections")
    conversation_history: List[dict[str, str]] = Field(default_factory=list, description="Conversation history")

    def get_conversation(self) -> list[dict[str, str]]:
        return self.conversation_history  

    def conversation_append(self, role: str, message: str):
        if role not in {"user", "assistant"}:
            return
        self.conversation_history.append(self._msg(role, message))     
        return self.conversation_history   

    def _msg(self,role: str, content: str) -> dict:
        return {"role": role, "content": content}  

    def get_section(self, section_id: SectionID) -> Optional[SectionContextBase]:
        #search through all main contexts to find section
        for context in self.main_contexts:
            for section in context.sections:
                if section.section_id == section_id:
                    return section
        raise ValueError(f"Section {section_id} not found in InterviewContext.")

    def get_current_section(self) -> Optional[SectionContextBase]:
        return self.get_section(self.section_id)

    def advance_to_next_section(self):
        self.section_id = self.section_id.next()

    def update_section(self, new_section: SectionContextBase) -> None:
        # Update the matching section within main_context(s)
        for mc in self.main_contexts:
            for idx, section in enumerate(mc.sections):
                if section.section_id == new_section.section_id:
                    mc.sections[idx] = new_section
                    return
        raise ValueError(f"Section {new_section.section_id} not found in InterviewContext.")