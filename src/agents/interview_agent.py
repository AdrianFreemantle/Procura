from openai import OpenAI
from agents.agent_prompts.prompts import build_prompt
from agents.context_management.interview_context import InterviewContext
from agents.context_management.session_contexts.contexts import SectionContextBase
import os

class InterviewerAgent:
    def __init__(self):
        self.client = OpenAI()
        self.model = os.getenv("INTERVIEW_MODEL", "gpt-4.1-mini")
        self.temperature = float(os.getenv("INTERVIEW_TEMP", 0.7))
        self.max_tokens = int(os.getenv("INTERVIEW_MAX_TOKENS", 1000))

    def interview(self, main_context: InterviewContext):
        context = main_context.get_current_section()
        input = main_context.get_conversation() + [self._msg("developer", self._build_developer_prompt(context))]
        
        with self.client.responses.stream(
            model=self.model,
            input=input,
            instructions=self._build_system_prompt(context),
            temperature=self.temperature,       
            max_output_tokens=self.max_tokens, 
        ) as stream:    
            yield from self._process_stream(stream, main_context)
    
    def _build_system_prompt(self, context: SectionContextBase):
        prompt = build_prompt(context.section_id, "interviewer")
        return prompt

    def _build_developer_prompt(self, context: SectionContextBase):
        prompt = context.model_dump_json(indent=1)
        return prompt

    def _process_stream(self, stream, main_context: InterviewContext):
        for event in stream:
            if event.type == "response.output_text.delta" and event.snapshot:
                yield main_context.get_conversation() + [self._msg("assistant", event.snapshot)]

        final_response = stream.get_final_response()

        try:
            if final_response.object == "response":
                main_context.conversation_append("assistant", final_response.output[0].content[0].text)
        except (IndexError, AttributeError, TypeError):
            pass  # TODO: log error

    def _msg(self,role: str, content: str) -> dict:
        return {"role": role, "content": content}                 