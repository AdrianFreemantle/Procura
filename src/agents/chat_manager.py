
from agents.context import Context
from agents.facts_agent import FactsAgent
from agents.interview_agent import InterviewerAgent

class ChatManager:
    def __init__(self):
        self.facts_agent = FactsAgent()
        self.interviewer_agent = InterviewerAgent()
        self.context = Context()

    def _msg(self,role: str, content: str) -> dict:
        return {"role": role, "content": content}    

    def chat(self, user_input: str):
        history = self.interviewer_agent.get_conversation_history()

        yield history + [self._msg("user", user_input), self._msg("assistant", "…thinking")]   
        
        self.context = self.facts_agent.evaluate(history, self.context)          
        
        yield from self.interviewer_agent.interview(user_input=user_input, context=self.context)  