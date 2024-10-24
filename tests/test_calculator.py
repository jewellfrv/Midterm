# tests/test_calculator.py

import pytest
from source.calculator import Calculator

def test_add():
    calculator = Calculator()
    assert calculator.add(3, 2) == 5
    assert calculator.add(-3, 3) == 0
    assert calculator.add(0, 0) == 0
    assert calculator.add(1.5, 2.5) == 4.0

def test_subtract():
    calculator = Calculator()
    assert calculator.subtract(5, 3) == 2
    assert calculator.subtract(-1, -1) == 0
    assert calculator.subtract(0, 3) == -3
    assert calculator.subtract(2.5, 1.0) == 1.5

def test_multiply():
    calculator = Calculator()
    assert calculator.multiply(4, 2) == 8
    assert calculator.multiply(-4, 2) == -8
    assert calculator.multiply(0, 5) == 0
    assert calculator.multiply(3.5, 2) == 7.0

def test_divide():
    calculator = Calculator()
    
    # Normal division
    assert calculator.divide(6, 3) == 2
    assert calculator.divide(7.5, 2.5) == 3

    # Division by zero should raise an exception
    with pytest.raises(ZeroDivisionError):
        calculator.divide(6, 0)
