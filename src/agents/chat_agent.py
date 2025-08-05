from agents.agent import Agent

class ChatAgent:
    def __init__(self, model="gpt-4.1-mini"):
        self.agent = Agent(model, chat_agent_system_prompt)

    def chat(self, user_input):
        yield from self.agent.send(user_input=user_input, developer_prompt="You speak like a pirate.", show_thinking=True, return_string_only=False)
        
chat_agent_system_prompt = ("You are a friendly assistant.")

