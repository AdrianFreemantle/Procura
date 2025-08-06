from enum import Enum

class SectionID(str, Enum):
    S101 = "S101"
    S102 = "S102"
    S103 = "S103"

class PromptRole(str, Enum):
    INTERVIEWER = "interviewer"
    FACT_EVALUATOR = "fact_evaluator"    