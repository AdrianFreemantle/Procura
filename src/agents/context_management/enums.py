from enum import Enum

class SectionID(str, Enum):
    S101 = "S101"
    S102 = "S102"
    S103 = "S103"
    EOF = "EOF"

    def __str__(self):
        return f"Section {self.value}"

    def next(self):
        members = list(self.__class__)
        idx = members.index(self)
        if idx + 1 >= len(members):
            raise StopIteration(f"{self} is the last enum member")
        return members[idx + 1] 