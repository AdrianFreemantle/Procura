from openai import OpenAI
from agents.prompts import S101_INTERVIEWER_PROMPT
from agents.context import Context

class InterviewerAgent:

    def __init__(self, model="gpt-4.1-mini", system_prompt: str = S101_INTERVIEWER_PROMPT):       
        self.client = OpenAI()
        self.model = model
        self.conversation_history = []
        self.allowed_conversation_roles = {"user", "assistant"}
        self.system_prompt = system_prompt
        self.temperature = 0.7
        #HACK: we populate the conversation history with the initial greeting here and in the ui.py to simplify the greeting process
        self.conversation_history.append(self._msg("assistant", "Hello! I am here to assist you in gathering information to draft an NEC4 Supply Short Contract."))

    def interview(self, user_input: str, context: Context):
        self.conversation_history.append(self._msg("user", user_input))        

        input = self.conversation_history + [self._msg("developer", context.model_dump_json())]
        
        with self.client.responses.stream(
            model=self.model,
            input=input,
            instructions=self.system_prompt,
            temperature=self.temperature            
        ) as stream:    
            yield from self._process_stream(stream)
    
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