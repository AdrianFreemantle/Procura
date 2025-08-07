import rich
from agents.facts_agent import FactsAgent
from agents.interview_agent import InterviewerAgent
from agents.context_management import Context

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

        rich.print(self.context.model_dump_json(indent=2))        
        yield from self.interviewer_agent.interview(user_input=user_input, context=self.context)  

        history = self.interviewer_agent.get_conversation_history()
        self.context = self.facts_agent.evaluate(history, self.context)         
        rich.print(self.context.model_dump_json(indent=2))