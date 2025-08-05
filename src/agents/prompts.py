from agents.constants import (
    INTERVIEWER_PROMPT,
    FACT_EVALUATOR_PROMPT,
    GENERAL_DEFINITIONS,
    SECTION_S101_DEFINITION,
    CONTEXT_JSON_SCHEMA,
    CONTEXT_JSON_CONVENTIONS
)

S101_INTERVIEWER_PROMPT = (INTERVIEWER_PROMPT 
                         + GENERAL_DEFINITIONS 
                         + SECTION_S101_DEFINITION 
                         + CONTEXT_JSON_CONVENTIONS)

S101_FACT_EVALUATOR_PROMPT = (FACT_EVALUATOR_PROMPT 
                            + GENERAL_DEFINITIONS 
                            + SECTION_S101_DEFINITION 
                            + CONTEXT_JSON_SCHEMA
                            + CONTEXT_JSON_CONVENTIONS)