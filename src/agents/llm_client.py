from openai import OpenAI
import os

class MockOpenAI:
    def __init__(self):
        self.chat = self._Chat()
        self.responses = self._Responses()

    class _Chat:
        def __init__(self):
            self.completions = self._Completions()

        class _Completions:
            def create(self, *args, **kwargs):
                class MockChoice:
                    def __init__(self):
                        self.message = self._Message()
                    class _Message:
                        def __init__(self):
                            self.content = "This is a mock response from the LLM."

                class MockCompletion:
                        def __init__(self):
                            self.choices = [MockChoice()]

                return MockCompletion()

    class _Responses:
        def parse(self, *, model, temperature, instructions, max_output_tokens, input, text_format):
            """Return an object with output_parsed matching the expected Pydantic model.
            We construct a default instance of text_format and set minimal helpful fields if present.
            """
            try:
                parsed = text_format()
                # Best-effort: populate a user-visible message if such a field exists
                if hasattr(parsed, "message_to_user"):
                    setattr(parsed, "message_to_user", "[mock] This is a mock parsed response.")
                return type("MockParsedResponse", (), {"output_parsed": parsed})()
            except Exception:
                # Fallback to a simple object with a dict if instantiation fails
                return type("MockParsedResponse", (), {"output_parsed": {"message_to_user": "[mock] parsed"}})()

        class _StreamContext:
            def __init__(self, chunks):
                self._chunks = chunks

            def __enter__(self):
                return self._iter()

            def __exit__(self, exc_type, exc, tb):
                return False

            def _iter(self):
                for piece in self._chunks:
                    yield type("MockEvent", (), {"type": "response.output_text.delta", "delta": piece})()

        def stream(self, *, model, temperature, max_output_tokens, instructions, input):
            """Return a context manager yielding mock streaming events compatible with _process_stream."""
            # Simple deterministic mock output based on instructions prefix
            content = "[mock stream] "
            # Append a tiny bit of the last user/dev content if available
            try:
                if input and isinstance(input, list) and isinstance(input[-1], dict):
                    content += str(input[-1].get("content", ""))[:30]
            except Exception:
                pass
            chunks = [content, " ...", " done"]
            return self._StreamContext(chunks)

def get_openai_client():
    if os.getenv("APP_ENV") == "test":
        print("Returning MOCK OpenAI client")
        return MockOpenAI()
    else:
        print("Returning REAL OpenAI client")
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError("The OPENAI_API_KEY environment variable is not set.")
        return OpenAI(api_key=api_key)