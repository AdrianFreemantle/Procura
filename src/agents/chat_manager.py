import logging
from agents.interview_agent import InterviewerAgent
from agents.document_drafting.drafter_agent import DrafterAgent

from agents.context_management.interview_context import InterviewContext
from agents.context_management.session_contexts.contexts import *
from agents.context_management.session_contexts.section_context import SectionStatus
from agents.context_management.persistence.sqlite_store import SqlLiteContextStore

import time
import rich
from datetime import datetime

logger = logging.getLogger(__name__)

class ChatManager:
    def __init__(self):    
        self.interviewer_agent = InterviewerAgent()
        self.drafter_agent = DrafterAgent()
        # Initialize an in-memory working context; persisted on first save
        self.persisted_context = InterviewContext(main_contexts=MAIN_CONTEXTS)
        self.context_store = SqlLiteContextStore()
        self.current_context_id: int | None = None
        logger.info("ChatManager initialized")
        
    def create_new_context(self, name: str | None = None) -> InterviewContext:
        """Create a new InterviewContext with status 'empty'.
        The context will be assigned an integer ID when first saved.
        """
        context = InterviewContext(
            context_id=None,
            context_name=name if name else datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            context_status="empty",
            main_contexts=MAIN_CONTEXTS
        )
        self.persisted_context = context
        logger.debug("Created new context with name '%s'", context.context_name)
        return context
    
    def load_context(self, context_id: int) -> InterviewContext | None:
        """Load an InterviewContext by integer ID from the store."""
        context = self.context_store.get_context(context_id)
        if context is not None:
            self.persisted_context = context
            self.current_context_id = context.context_id
            logger.debug("Loaded context id=%s name='%s' status=%s", context.context_id, context.context_name, context.context_status)
        else:
            logger.warning("Context id=%s not found when attempting to load", context_id)
        return context

    def save_context(self, context: InterviewContext) -> int:
        """Persist the context to the store and update current_context_id.
        Returns the assigned integer context_id.
        """
        context_id = self.context_store.store_context(context)
        self.persisted_context = context
        self.current_context_id = context_id
        logger.debug("Saved context id=%s name='%s' status=%s", context_id, context.context_name, context.context_status)
        return context_id
        
    def _msg(self,role: str, content: str) -> dict:
        return {"role": role, "content": content}    

    def get_greeting_message(self) -> str:
        """Generate a greeting message for new chats."""
        return """👋 Welcome to Procura - Your NEC4 SSC Scope Document Assistant!

What specific operational issue, deficiency, or risk tied to the Purchaser's operations is prompting this procurement?        
        """

    def chat(self, user_input: str): 
        # Ensure there is a working context
        context = self.persisted_context
        if context is None:
            context = self.create_new_context()

        if(user_input.startswith("/")):
            if(user_input.strip() == "/context"):
                section = context.get_current_section()
                yield context.get_conversation() + [self._msg("user", user_input), self._msg("assistant", section.model_dump_json(indent=1))]
                return

        # First user interaction activates the context
        if context.context_status == "empty":
            context.context_status = "active"
            logger.debug("Context id=%s promoted to 'active'", context.context_id)

        logger.info("User input: %s", user_input)
        context.conversation_append("user", user_input)

        start_time = time.perf_counter()
        new_context = self.interviewer_agent.evaluate(context)    
        logger.info("New context: %s", new_context.model_dump_json())        
        end_time = time.perf_counter()   
        logger.debug("Facts evaluation took %.2f seconds", (end_time - start_time))          

        context.update_section(new_context)        

        rich.print(new_context)
        rich.print("Facts evaluation seconds", (end_time - start_time))  
        context.conversation_append("assistant", new_context.message_to_user)
        new_context.message_to_user = "" #clear message after it has been saved
        yield context.get_conversation()            


        if new_context.section_status == SectionStatus.complete:            
            context.advance_to_next_section()                       
        
        # Persist updates and ensure an integer ID is assigned
        self.save_context(context)

    def switch_context(self, context_id: int) -> InterviewContext | None:
        """Switch the active conversation to the specified context ID."""
        ctx = self.load_context(context_id)
        if ctx is not None:
            logger.info("Switched to context id=%s", context_id)
        return ctx

    def draft(self):
        yield from self.drafter_agent.draft(self.persisted_context)

    def list_contexts(self):
        """List contexts for UI selection, filtering out 'empty' except the current context."""
        current_id = self.current_context_id if self.current_context_id is not None else None
        logger.debug("Listing contexts (current_context_id=%s)", current_id)
        return self.context_store.list_contexts(current_id)