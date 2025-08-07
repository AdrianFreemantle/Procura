from enum import Enum

class SectionID(str, Enum):
    S101 = "S101"
    S102 = "S102"
    S103 = "S103"

    def __str__(self):
        return f"Section {self.value}"

class PromptRole(str, Enum):
    INTERVIEWER = "interviewer"
    FACT_EVALUATOR = "fact_evaluator"    