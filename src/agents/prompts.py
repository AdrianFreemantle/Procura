from agents.constants import (
    INTERVIEWER_PROMPT,
    FACT_EVALUATOR_PROMPT,
    GENERAL_DEFINITIONS,
    SECTION_S100_DEFINITION,
    CONTEXT_JSON_SCHEMA,
    CONTEXT_JSON_DESCRIPTION
)

S100_INTERVIEWER_PROMPT = (INTERVIEWER_PROMPT 
                         + GENERAL_DEFINITIONS 
                         + SECTION_S100_DEFINITION 
                         + CONTEXT_JSON_DESCRIPTION)

S100_FACT_EVALUATOR_PROMPT = (FACT_EVALUATOR_PROMPT 
                            + GENERAL_DEFINITIONS 
                            + SECTION_S100_DEFINITION 
                            + CONTEXT_JSON_SCHEMA
                            + CONTEXT_JSON_DESCRIPTION)