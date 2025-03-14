# calculator/calculation_factory.py
from calculator.calculation import Calculation

class CalculationFactory:
    """
    Factory for creating Calculation objects.
    This factory method encapsulates the logic for instantiating Calculation objects
    based on the provided operator.
    """
    @staticmethod
    def create_calculation(a: float, b: float, operator: str) -> Calculation:
        if operator not in ['+', '-', '*', '/']:
            raise ValueError(f"Unsupported operator: {operator}")
        return Calculation(a, b, operator)
