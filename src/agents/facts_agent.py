from openai import OpenAI
from pydantic import BaseModel, Field
import rich
from agents.prompts import S100_FACT_EVALUATOR_PROMPT, S100_INTERVIEWER_PROMPT

###########################################
class Facts(BaseModel):
    business_need: str = Field(default="", description="Business need")
    problem_statement: str = Field(default="", description="Problem statement")
    safety_objectives: str = Field(default="", description="Safety objectives")
    quality_objectives: str = Field(default="", description="Quality objectives")
    delivery_time_objectives: str = Field(default="", description="Delivery time objectives")
    operational_improvement_objectives: str = Field(default="", description="Operational improvement objectives")
    outcome: str = Field(default="", description="Expected outcome")
    benefits: str = Field(default="", description="Expected benefits")
    replaced_assets: str = Field(default="", description="Assets to be replaced")
    location_context: str = Field(default="", description="Location context")
    compliance_targets: str = Field(default="", description="Compliance targets")
    custom_facts: str = Field(default="", description="Additional custom facts as JSON string or text")

###########################################
class Context(BaseModel):
    next_question: str = Field(default="", description="Next question to ask")
    facts: Facts = Field(default_factory=Facts, description="Facts extracted from the conversation")

###########################################
class ChatManager:
    def __init__(self):
        self.facts_agent = FactsAgent()
        self.interviewer_agent = InterviewerAgent()
        self.context = Context()

    def _msg(self,role: str, content: str) -> dict:
        return {"role": role, "content": content}    

    def chat(self, user_input: str):
        history = self.interviewer_agent.get_conversation_history()

        yield history + [self._msg("user", user_input), self._msg("assistant", "…thinking")]   
        
        self.context = self.facts_agent.evaluate(history, self.context)          
        
        yield from self.interviewer_agent.interview(user_input=user_input, context=self.context)           

###########################################
class FactsAgent:
    def __init__(self, model="gpt-4.1-mini", system_prompt: str = S100_FACT_EVALUATOR_PROMPT):
        self.client = OpenAI()
        self.model = model
        self.conversation_history = []
        self.system_prompt = system_prompt

    def evaluate(self, history: list[dict[str, str]], context: Context) -> Context:
        rich.print(context.model_dump_json(indent=2))

        response = self.client.responses.parse(            
            model=self.model,            
            temperature=0.0,
            instructions=self.system_prompt,
            input=[
                self._msg("developer", context.model_dump_json()),
                self._msg("user", "get facts")
            ] + history,
            text_format=Context
        )

        new_context = response.output_parsed
        
        rich.print(new_context.model_dump_json(indent=2))
        
        return new_context

    def _msg(self,role: str, content: str) -> dict:
        return {"role": role, "content": content} 

###########################################
class InterviewerAgent:
    def __init__(self, model="gpt-4.1-mini", system_prompt: str = S100_INTERVIEWER_PROMPT):       
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