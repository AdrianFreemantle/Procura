from openai import OpenAI
import rich

def msg(role: str, content: str) -> dict:
    return {"role": role, "content": content}        

class ChatAgent:
    def __init__(self, model="gpt-4.1"):
        self.client = OpenAI()
        self.model = model
        self.history = []
        self.allowed_roles = {"user", "assistant"}

    def chat(self, user_input):
        # Add user message to history
        self.history.append(msg("user", user_input))

        yield self.format_history() + [msg("assistant", "…thinking")]            

        with self.client.responses.stream(
            model=self.model,
            input=self.history,
            instructions="You are a helpful assistant."            
        ) as stream:
            yield from self._process_stream(stream)
    
    def _process_stream(self, stream):
        for event in stream:
            if event.type == "response.output_text.delta" and event.snapshot:
                rich.print(event)
                yield self.format_history() + [msg("assistant", event.snapshot)]

        final_response = stream.get_final_response()

        try:
            if final_response.object == "response":
                self.history.append(msg("assistant", final_response.output[0].content[0].text))
        except (IndexError, AttributeError, TypeError):
            pass  # TODO: log error

    def format_history(self):
        formatted = []
        for message in self.history:
            role = message.get("role")
            if role not in self.allowed_roles:
                continue
            content = message.get("content", "")
            formatted.append(msg(role, content))
        return formatted

    def reset(self):
        self.history = []
