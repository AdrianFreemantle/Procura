from openai import OpenAI
from agents.context_management import *
from agents.agent_prompts import *
from agents.agent_prompts.base_prompts import *
from agents.context_management.interview_context import InterviewContext
from agents.context_management.session_contexts.section_context import *
from agents.document_drafting.style_guides.document_styles import DOCUMENTATION_STYLES
import os
import rich

class DrafterAgent:
    def __init__(self):
        self.client = OpenAI()
        self.model = os.getenv("INTERVIEW_MODEL", "gpt-4.1-mini")
        self.temperature =  0.0
        self.max_tokens = 50000

    def draft(self, interview_context: InterviewContext):     
        for main_context in interview_context.main_contexts:
            rich.print(main_context.id + ": " + main_context.name)
            yield "# " + main_context.id + ": " + main_context.name + "\n"
            for section_context in main_context.sections:
                if section_context.section_status == SectionStatus.complete:
                    yield from self.draft_section(section_context)  
                    yield "\n"   

    def draft_section(self, section: SectionContextBase):  
        sys_prompt = DRAFTER_SYSTEM_PROMPT + "\n\n" + DOCUMENTATION_STYLES.section_style[section.section_id].system_prompt() + DOCUMENTATION_STYLES.section_style[section.section_id].developer_prompt()
            
        with self.client.responses.stream(            
            model=self.model,            
            temperature=self.temperature,
            max_output_tokens=self.max_tokens,
            instructions=sys_prompt,
            input=[          
                self._msg("developer", DRAFTER_DEVELOPER_PROMPT),
                self._msg("user", section.model_dump_json())
            ]   
        ) as stream:
            yield from self._process_stream(stream)
        
    def _process_stream(self, stream):
        for event in stream:
            if event.type == "response.output_text.delta":
                yield event.delta        

    def _msg(self,role: str, content: str) -> dict:
        return {"role": role, "content": content} 
