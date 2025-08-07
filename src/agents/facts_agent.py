from openai import OpenAI
from agents.context_management import *

import os

class FactsAgent:
    def __init__(self):
        self.client = OpenAI()
        self.model = os.getenv("FACTS_MODEL", "gpt-4.1-mini")
        self.temperature = float(os.getenv("FACTS_TEMP", 0.0))
        self.conversation_history = []

    def evaluate(self, history: list[dict[str, str]], context: Context) -> Context:      
        response = self.client.responses.parse(            
            model=self.model,            
            temperature=self.temperature,
            instructions=self._build_system_prompt(context.current_section),
            input=[
                self._msg("developer", context.model_dump_json()),
                self._msg("user", "get facts")
            ] + history,
            text_format=Context
        )

        new_context = response.output_parsed
        
        return new_context

    def _build_system_prompt(self, section_id: SectionID):
        return build_prompt(section_id, "fact_evaluator")

    def _msg(self,role: str, content: str) -> dict:
        return {"role": role, "content": content} 
