"""Module providing a function python version."""
# tests/test_calculation_factory.py
import pytest
from calculator.calculation_factory import CalculationFactory

def test_create_calculation_invalid_operator():
    """
    Test that creating a Calculation with an unsupported operator
    raises a ValueError with the expected message.
    """
    with pytest.raises(ValueError) as excinfo:
        CalculationFactory.create_calculation(1, 2, "^")
    assert "Unsupported operator: ^" in str(excinfo.value)
