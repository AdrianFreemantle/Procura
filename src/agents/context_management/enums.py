from enum import Enum

# -----------------------------
# Enums (single source of truth)
# -----------------------------

class MainSectionID(str, Enum):
    S100 = "S100"
    S200 = "S200"
    S300 = "S300"
    S400 = "S400"
    S500 = "S500"
    S600 = "S600"
    EOF = "EOF"

    def __str__(self):
        return f"Section {self.value}"

    def next(self):
        members = list(self.__class__)
        idx = members.index(self)
        if idx + 1 >= len(members):
            raise StopIteration(f"{self} is the last enum member")
        return members[idx + 1]     

class SectionID(str, Enum):
    S101 = "S101"
    S102 = "S102"
    S103 = "S103"
    S104 = "S104"
    S105 = "S105"
    S106 = "S106"
    S107 = "S107"
    S108 = "S108"
    S109 = "S109"
    S110 = "S110"
    S111 = "S111"
    S112 = "S112"
    S201 = "S201"
    S202 = "S202"
    S301 = "S301"
    S302 = "S302"
    S303 = "S303"
    S304 = "S304"
    S305 = "S305"
    S306 = "S306"
    S307 = "S307"
    S308 = "S308"
    S309 = "S309"
    S310 = "S310"
    S311 = "S311"
    S312 = "S312"
    S313 = "S313"
    EOF = "EOF"

    def __str__(self):
        return f"Section {self.value}"

    def next(self):
        members = list(self.__class__)
        idx = members.index(self)
        if idx + 1 >= len(members):
            raise StopIteration(f"{self} is the last enum member")
        return members[idx + 1] 