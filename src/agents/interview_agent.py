from openai import OpenAI
from agents.context_management import *
from agents.agent_prompts.prompts import build_prompt
from agents.context_management.interview_context import InterviewContext
from agents.context_management.session_contexts.contexts import SectionContextBase, SECTION_CONTEXT_TYPES

import os

class InterviewerAgent:
    def __init__(self):
        self.client = OpenAI()
        self.model = os.getenv("INTERVIEW_MODEL", "gpt-4.1-mini")
        self.temperature = float(os.getenv("INTERVIEW_TEMP", 0.0))
        self.max_tokens = int(os.getenv("INTERVIEW_MAX_TOKENS", 1000))
        self.conversation_history = []

    def evaluate(self, main_context: InterviewContext) -> SectionContextBase:      
        context = main_context.get_current_section()
        response = self.client.responses.parse(            
            model=self.model,            
            temperature=self.temperature,
            instructions=self._build_system_prompt(context.section_id),
            max_output_tokens=self.max_tokens,
            input=[
                self._msg("developer", context.model_dump_json()),
                self._msg("user", "get facts")
            ] + main_context.get_conversation(),
            text_format=SECTION_CONTEXT_TYPES[context.section_id]            
        )
        
        new_context = response.output_parsed        
        
        return new_context

    def _build_system_prompt(self, section_id: SectionID):
        return build_prompt(section_id)

    def _msg(self,role: str, content: str) -> dict:
        return {"role": role, "content": content} 
