from openai import OpenAI
from agents.context_management import *
from agents.agent_prompts.prompts import build_prompt
from agents.context_management.session_contexts.contexts import SectionContextBase, SECTION_CONTEXT_TYPES

import os

class FactsAgent:
    def __init__(self):
        self.client = OpenAI()
        self.model = os.getenv("FACTS_MODEL", "gpt-4.1-mini")
        self.temperature = float(os.getenv("FACTS_TEMP", 0.0))
        self.max_tokens = int(os.getenv("FACTS_MAX_TOKENS", 1000))
        self.conversation_history = []

    def evaluate(self, history: list[dict[str, str]], context: SectionContextBase) -> SectionContextBase:      
        response = self.client.responses.parse(            
            model=self.model,            
            temperature=self.temperature,
            instructions=self._build_system_prompt(context.section_id),
            max_output_tokens=self.max_tokens,
            input=[
                self._msg("developer", context.model_dump_json()),
                self._msg("user", "get facts")
            ] + history,
            text_format=SECTION_CONTEXT_TYPES[context.section_id]            
        )
        
        new_context = response.output_parsed        
        
        return new_context

    def _build_system_prompt(self, section_id: SectionID):
        return build_prompt(section_id, "fact_evaluator")

    def _msg(self,role: str, content: str) -> dict:
        return {"role": role, "content": content} 
