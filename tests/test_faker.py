"""Module providing a function python version."""
# tests/test_faker.py
from faker import Faker
from calculator.calculator import Calculator

def test_faker_addition():
    """Faker test module"""
    fake = Faker()
    # Generate two random integers between 1 and 100
    a = fake.random_int(min=1, max=100)
    b = fake.random_int(min=1, max=100)
    expected = a + b
    result = Calculator.add(float(a), float(b))
    assert result == expected
