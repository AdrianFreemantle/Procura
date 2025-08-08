import rich
from agents.facts_agent import FactsAgent
from agents.interview_agent import InterviewerAgent
from agents.context_management.interview_context import InterviewContext
from agents.context_management.session_contexts.contexts import CONTEXTS
from agents.context_management.persistence.sqlite_store import SqlLiteContextStore
import time
from datetime import datetime

class ChatManager:
    def __init__(self):
        self.facts_agent = FactsAgent()                
        self.interviewer_agent = InterviewerAgent()
        # Initialize an in-memory working context; persisted on first save
        self.persisted_context = InterviewContext()
        self.persisted_context.sections = CONTEXTS
        self.context_store = SqlLiteContextStore()
        self.current_context_id: int | None = None
        
    def create_new_context(self, name: str | None = None) -> InterviewContext:
        """Create a new InterviewContext with status 'empty'.
        The context will be assigned an integer ID when first saved.
        """
        context = InterviewContext(
            context_id=None,
            context_name=name if name else datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            context_status="empty",
            sections=CONTEXTS
        )
        self.persisted_context = context
        return context
    
    def load_context(self, context_id: int) -> InterviewContext | None:
        """Load an InterviewContext by integer ID from the store."""
        context = self.context_store.get_context(context_id)
        if context is not None:
            self.persisted_context = context
            self.current_context_id = context.context_id
        return context

    def save_context(self, context: InterviewContext) -> int:
        """Persist the context to the store and update current_context_id.
        Returns the assigned integer context_id.
        """
        context_id = self.context_store.store_context(context)
        self.persisted_context = context
        self.current_context_id = context_id
        return context_id
        
    def _msg(self,role: str, content: str) -> dict:
        return {"role": role, "content": content}    

    def chat(self, user_input: str): 
        # Ensure there is a working context
        context = self.persisted_context
        if context is None:
            context = self.create_new_context()

        # First user interaction activates the context
        if context.context_status == "empty":
            context.context_status = "active"

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

        # Persist updates and ensure an integer ID is assigned
        self.save_context(context)

    def switch_context(self, context_id: int) -> InterviewContext | None:
        """Switch the active conversation to the specified context ID."""
        ctx = self.load_context(context_id)
        return ctx

    def list_contexts(self):
        """List contexts for UI selection, filtering out 'empty' except the current context."""
        return self.context_store.list_contexts(self.current_context_id if self.current_context_id is not None else None)