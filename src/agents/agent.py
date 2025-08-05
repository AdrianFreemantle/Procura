from openai import OpenAI

def msg(role: str, content: str) -> dict:
    return {"role": role, "content": content}        

class Agent:
    def __init__(self, model="gpt-4.1"):
        self.client = OpenAI()
        self.model = model
        self.conversation_history = []
        self.allowed_conversation_roles = {"user", "assistant"}

    def chat(self, user_input: str, instructions: str = "You are a helpful assistant.", context: str = None):       
                           
        self.conversation_history.append(msg("user", user_input))        

        yield self.get_conversation_history() + [msg("assistant", "…thinking")]      

        messages = self.conversation_history

        if(context):
            messages = messages + [msg("developer", context)]
        
        with self.client.responses.stream(
            model=self.model,
            input=messages,
            instructions=instructions            
        ) as stream:
            yield from self._process_stream(stream)
    
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
