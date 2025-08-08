import rich
from agents.facts_agent import FactsAgent
from agents.interview_agent import InterviewerAgent
from agents.context_management.interview_context import InterviewContext
from agents.context_management.session_contexts.contexts import CONTEXTS
from agents.context_management.persistence.sqlite_store import SqlLiteContextStore
import time

class ChatManager:
    def __init__(self):
        self.facts_agent = FactsAgent()                
        self.interviewer_agent = InterviewerAgent()
        self.persisted_context = InterviewContext()
        self.persisted_context.sections = CONTEXTS
        self.context_store = SqlLiteContextStore()
        
    def create_context(self, context_id: str) -> InterviewContext:        
        return InterviewContext(context_id=context_id, sections=CONTEXTS)
    
    def load_context(self, context_id: str) -> InterviewContext:
        #TODO: load from SqlLiteContextStore
        return self.persisted_context        

    def save_context(self, context: InterviewContext) -> None:
        #TODO: save to SqlLiteContextStore
        self.persisted_context = context
        
    def _msg(self,role: str, content: str) -> dict:
        return {"role": role, "content": content}    

    def chat(self, user_input: str): 
        context = self.load_context("1")

        if(context is None):
            context = self.create_context("1")

        context.conversation_append("user", user_input)

        start_time = time.perf_counter()
        new_context = self.facts_agent.evaluate(context)            
        rich.print("FACTS AGENT OUTPUT: " + new_context.model_dump_json(indent=1))     
        end_time = time.perf_counter()   
        print(f"Facts call took {end_time - start_time:.2f} seconds")

        context.update_section(new_context)        
        if new_context.section_status == "complete":
            context.advance_to_next_section()                     

        start_time = time.perf_counter()
        yield from self.interviewer_agent.interview(context)               
        end_time = time.perf_counter()
        print(f"Interview call took {end_time - start_time:.2f} seconds")

        self.save_context(context)