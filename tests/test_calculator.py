'''This is a test file for my calculator program'''
from calculator import add, subtract

def test_addition():
    '''Addition Test'''
    assert add(2,2) == 4

def test_subtraction():
    '''Subtraction Test'''
    assert subtract(2,2) == 0
