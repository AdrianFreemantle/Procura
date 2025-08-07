import rich
from agents.facts_agent import FactsAgent
from agents.interview_agent import InterviewerAgent
from agents.context_management.interview_context import InterviewContext

class ChatManager:
    def __init__(self):
        self.facts_agent = FactsAgent()        
        self.context = InterviewContext()
        self.interviewer_agent = InterviewerAgent()

    def _msg(self,role: str, content: str) -> dict:
        return {"role": role, "content": content}    

    def chat(self, user_input: str):
        self.context.print_current_section()

        history = self.interviewer_agent.get_conversation_history()
        yield history + [self._msg("user", user_input), self._msg("assistant", "…thinking")]                                    
        yield from self.interviewer_agent.interview(user_input=user_input, context=self.context.get_current_section())               
                
        new_context = self.facts_agent.evaluate(self.interviewer_agent.get_conversation_history(), self.context.get_current_section())         
        self.context.update_section(new_context)
        self.context.print_current_section()