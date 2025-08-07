import rich
from agents.facts_agent import FactsAgent
from agents.interview_agent import InterviewerAgent
from agents.context_management.interview_context import InterviewContext
from agents.context_management.session_contexts.contexts import CONTEXTS

class ChatManager:
    def __init__(self):
        self.facts_agent = FactsAgent()        
        self.context = InterviewContext()
        self.context.sections = CONTEXTS
        self.interviewer_agent = InterviewerAgent()

    def _msg(self,role: str, content: str) -> dict:
        return {"role": role, "content": content}    

    def chat(self, user_input: str):
        #rich.print("USER INPUT: " + user_input)        
        self.context.print_current_section()

        history = self.interviewer_agent.get_conversation_history()
        yield history + [self._msg("user", user_input), self._msg("assistant", "…thinking")]                                    
        yield from self.interviewer_agent.interview(user_input=user_input, context=self.context.get_current_section())               
                
        new_context = self.facts_agent.evaluate(self.interviewer_agent.get_conversation_history(), self.context.get_current_section())    
        self.context.update_section(new_context)

        if new_context.section_status == "complete":
            self.context.next_section()

        self.context.print_current_section()
             
        rich.print("FACTS AGENT OUTPUT: " + new_context.model_dump_json(indent=1))
        self.context.update_section(new_context)