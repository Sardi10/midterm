# calculator/calculator.py
from .calculation import Calculation

class Calculator:
    """
    Provides static methods for basic arithmetic operations.
    """
    @staticmethod
    def add(a: float, b: float) -> float:
        calc = Calculation(a, b, '+')
        return calc.perform()

    @staticmethod
    def subtract(a: float, b: float) -> float:
        calc = Calculation(a, b, '-')
        return calc.perform()

    @staticmethod
    def multiply(a: float, b: float) -> float:
        calc = Calculation(a, b, '*')
        return calc.perform()

    @staticmethod
    def divide(a: float, b: float) -> float:
        calc = Calculation(a, b, '/')
        return calc.perform()
