import rich
from agents.facts_agent import FactsAgent
from agents.interview_agent import InterviewerAgent
from agents.context_management.interview_context import InterviewContext
from agents.context_management.session_contexts.contexts import CONTEXTS

import time

class ChatManager:
    def __init__(self):
        self.facts_agent = FactsAgent()        
        self.context = InterviewContext()
        self.context.sections = CONTEXTS
        self.interviewer_agent = InterviewerAgent()

    def _msg(self,role: str, content: str) -> dict:
        return {"role": role, "content": content}    

    def chat(self, user_input: str): 
        self.context.conversation_append("user", user_input)

        start_time = time.perf_counter()
        new_context = self.facts_agent.evaluate(self.context)            
        rich.print("FACTS AGENT OUTPUT: " + new_context.model_dump_json(indent=1))     
        end_time = time.perf_counter()   
        print(f"Facts call took {end_time - start_time:.2f} seconds")

        self.context.update_section(new_context)        
        if new_context.section_status == "complete":
            self.context.advance_to_next_section()                     

        start_time = time.perf_counter()
        yield from self.interviewer_agent.interview(self.context)               
        end_time = time.perf_counter()
        print(f"Interview call took {end_time - start_time:.2f} seconds")