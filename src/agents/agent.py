from openai import OpenAI

def msg(role: str, content: str) -> dict:
    return {"role": role, "content": content}        

class Agent:
    def __init__(self, model="gpt-4.1", temperature: float = 0.7, system_prompt: str ="You are a helpful assistant."):
        self.client = OpenAI()
        self.model = model
        self.conversation_history = []
        self.allowed_conversation_roles = {"user", "assistant"}
        self.system_prompt = system_prompt
        self.temperature = temperature

    def send(self, user_input: str = "Say hello", developer_prompt: str = None, show_thinking: bool = False, return_string_only: bool = False):                                  
        self.conversation_history.append(msg("user", user_input))        

        if(show_thinking):
            yield self.get_conversation_history() + [msg("assistant", "…thinking")]      

        input = self.conversation_history

        if(developer_prompt):
            input = input + [msg("developer", developer_prompt)]
        
        with self.client.responses.stream(
            model=self.model,
            input=input,
            instructions=self.system_prompt,
            temperature=self.temperature            
        ) as stream:    
            if(return_string_only):
                yield from self._process_stream_string_only(stream)
            else:
                yield from self._process_stream(stream)
    
    def _process_stream_string_only(self, stream):
        for event in stream:
            if event.type == "response.output_text.delta" and event.snapshot:
                yield event.snapshot

    def _process_stream(self, stream):
        for event in stream:
            if event.type == "response.output_text.delta" and event.snapshot:
                yield self.get_conversation_history() + [msg("assistant", event.snapshot)]

        final_response = stream.get_final_response()

        try:
            if final_response.object == "response":
                self.conversation_history.append(msg("assistant", final_response.output[0].content[0].text))
        except (IndexError, AttributeError, TypeError):
            pass  # TODO: log error

    def get_conversation_history(self):
        formatted = []
        for message in self.conversation_history:
            role = message.get("role")
            if role not in self.allowed_conversation_roles:
                continue
            content = message.get("content", "")
            formatted.append(msg(role, content))
        return formatted

    def reset(self):
        self.history = []
