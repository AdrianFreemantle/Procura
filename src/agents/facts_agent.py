from openai import OpenAI
import rich
from agents.prompts import S101_FACT_EVALUATOR_PROMPT, S101_INTERVIEWER_PROMPT
from agents.context import Context

class FactsAgent:
    def __init__(self, model="gpt-4.1-mini", system_prompt: str = S101_FACT_EVALUATOR_PROMPT):
        self.client = OpenAI()
        self.model = model
        self.conversation_history = []
        self.system_prompt = system_prompt

    def evaluate(self, history: list[dict[str, str]], context: Context) -> Context:
        rich.print(context.model_dump_json(indent=2))

        response = self.client.responses.parse(            
            model=self.model,            
            temperature=0.0,
            instructions=self.system_prompt,
            input=[
                self._msg("developer", context.model_dump_json()),
                self._msg("user", "get facts")
            ] + history,
            text_format=Context
        )

        new_context = response.output_parsed
        
        rich.print(new_context.model_dump_json(indent=2))
        
        return new_context

    def _msg(self,role: str, content: str) -> dict:
        return {"role": role, "content": content} 
