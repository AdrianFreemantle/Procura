from pydantic import BaseModel, Field

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

class Context(BaseModel):
    next_question: str = Field(default="", description="Next question to ask")
    current_section: str = Field(default="", description="Current section of the NEC4 SSC contract")
    facts: Facts = Field(default_factory=Facts, description="Facts extracted from the conversation")