from openai import OpenAI
from agents.agent_prompts.prompts import build_prompt
from agents.context_management.enums import SectionID
from agents.context_management.session_contexts.contexts import SectionContextBase
import os

class InterviewerAgent:
    def __init__(self):
        self.client = OpenAI()
        self.model = os.getenv("INTERVIEW_MODEL", "gpt-4.1-mini")
        self.temperature = float(os.getenv("INTERVIEW_TEMP", 0.7))
        self.conversation_history = []
        self.allowed_conversation_roles = {"user", "assistant"}

    def interview(self, user_input: str, context: SectionContextBase):
        self.conversation_history.append(self._msg("user", user_input))             

        input = self.conversation_history + [self._msg("developer", self._build_developer_prompt(context))]
        
        with self.client.responses.stream(
            model=self.model,
            input=input,
            instructions=self._build_system_prompt(context),
            temperature=self.temperature            
        ) as stream:    
            yield from self._process_stream(stream)
    
    def _build_system_prompt(self, context: SectionContextBase):
        prompt = build_prompt(context.section_id, "interviewer")
        #rich.print("SYSTEM PROMPT: " + prompt)
        return prompt

    def _build_developer_prompt(self, context: SectionContextBase):
        prompt = context.model_dump_json(indent=1)
        #rich.print("DEVELOPER PROMPT: " + prompt)
        return prompt

    def _process_stream(self, stream):
        for event in stream:
            if event.type == "response.output_text.delta" and event.snapshot:
                yield self.get_conversation_history() + [self._msg("assistant", event.snapshot)]

        final_response = stream.get_final_response()

        try:
            if final_response.object == "response":
                self.conversation_history.append(self._msg("assistant", final_response.output[0].content[0].text))
        except (IndexError, AttributeError, TypeError):
            pass  # TODO: log error

    def get_conversation_history(self):
        formatted = []
        for message in self.conversation_history:
            role = message.get("role")
            if role not in self.allowed_conversation_roles:
                continue
            content = message.get("content", "")
            formatted.append(self._msg(role, content))
        return formatted        

    def reset(self):
        self.conversation_history = []

    def _msg(self,role: str, content: str) -> dict:
        return {"role": role, "content": content}    