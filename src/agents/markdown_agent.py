from openai import OpenAI
client = OpenAI()

class MarkdownAgent:
    def __init__(self, model="gpt-4.1-mini"):
        self.agent = Agent(model)
        self.client = OpenAI()
        self.model = model

    def generate(self):
        stream = self.client.responses.create(
            model=self.model,
            input=[
                {
                    "role": "system",
                    "content": (
                        "You are a professional technical writer. "
                        "Generate a well-structured markdown document for a construction project summary. "
                        "Include headers, bullet points, and numbered lists."
                    ),
                },
                {
                    "role": "user",
                    "content": "Generate an example markdown document for a new construction project proposal.",
                },
            ],
            stream=True,
        )

        buffer = ""
        for chunk in stream:
            if chunk.choices and chunk.choices[0].delta:
                delta = chunk.choices[0].delta
                if delta.content:
                    buffer += delta.content
                    yield buffer
