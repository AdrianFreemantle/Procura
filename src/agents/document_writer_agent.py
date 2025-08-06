from openai import OpenAI
from agents.context import Context
from agents.prompts import build_prompt
from agents.enums import SectionID

class DocumentWriterAgent:
    def __init__(self, model="gpt-4.1-mini"):
        self.agent = Agent(model, draft_agent_system_prompt)

    def generate(self, context: Context) -> Context:
            

