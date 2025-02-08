# calculator/calculations.py
from typing import List, Tuple
from .calculation import Calculation

class Calculations:
    """
    Manages a history of Calculation instances.
    """
    def __init__(self) -> None:
        self.history: List[Calculation] = []

    def add_calculation(self, calculation: Calculation) -> None:
        self.history.append(calculation)

    def get_last(self) -> Calculation:
        if not self.history:
            raise IndexError("No calculations in history")
        return self.history[-1]

    def clear_history(self) -> None:
        self.history.clear()

    @classmethod
    def from_operations(cls, operations: List[Tuple[float, str, float]]) -> 'Calculations':
        instance = cls()
        for operand1, operator, operand2 in operations:
            calc = Calculation(operand1, operand2, operator)
            calc.perform()
            instance.add_calculation(calc)
        return instance
