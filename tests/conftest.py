"""Module providing a function python version."""
# tests/conftest.py
from random import choice
import pytest
from faker import Faker

def pytest_addoption(parser):
    """Addoption module"""
    parser.addoption(
        "--num_records",
        action="store",
        default=0,
        help="Generate N fake test records."
    )

@pytest.fixture(scope="session")
def fake_records(pytestconfig):
    """FAke test module"""
    num_records = int(pytestconfig.getoption("--num_records"))
    if num_records <= 0:
        return []  # No fake records generated if not specified

    fake = Faker()
    operations = ['+', '-', '*', '/']
    records = []

    for _ in range(num_records):
        # Generate two random integers
        a = fake.random_int(min=1, max=100)
        b = fake.random_int(min=1, max=100)
        op = choice(operations)
        # Handle divide by zero
        if op == '/' and b == 0:
            b = fake.random_int(min=1, max=100)
        expected = None
        try:
            if op == '+':
                expected = a + b
            elif op == '-':
                expected = a - b
            elif op == '*':
                expected = a * b
            elif op == '/':
                expected = a / b
        except ValueError:
            pass

        records.append((a, b, op, expected))
    return records
