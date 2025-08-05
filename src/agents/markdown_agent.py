from agents.agent import Agent

class MarkdownAgent:
    def __init__(self, model="gpt-4.1-mini"):
        self.agent = Agent(model, markdown_agent_system_prompt)

    def generate(self):
        yield "…thinking"
        yield from self.agent.send(user_input="Generate an example markdown document for a new construction project proposal.", string_only=True, show_thinking=False)


markdown_agent_system_prompt = (
 "You are a professional technical writer. "
 "You create well-structured markdown documents."
 "Include headers, bullet points, and numbered lists."
)