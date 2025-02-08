# calculator/calculation.py
# pylint: disable=unnecessary-dunder-call, invalid-name
from typing import Union

class Calculation:
    """
    Represents a single arithmetic calculation.
    """
    def __init__(self, operand1: float, operand2: float, operator: str) -> None:
        self.operand1: float = operand1
        self.operand2: float = operand2
        self.operator: str = operator
        self.result: Union[float, None] = None

    def perform(self) -> float:
        if self.operator == '+':
            self.result = self.operand1 + self.operand2
        elif self.operator == '-':
            self.result = self.operand1 - self.operand2
        elif self.operator == '*':
            self.result = self.operand1 * self.operand2
        elif self.operator == '/':
            if self.operand2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            self.result = self.operand1 / self.operand2
        else:
            raise ValueError(f"Invalid operator: {self.operator}")
        return self.result

    def __str__(self) -> str:
        return f"{self.operand1} {self.operator} {self.operand2} = {self.result}"
