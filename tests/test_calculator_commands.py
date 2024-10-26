# Tests for calculator command classes including AddCommand, SubtractCommand, MultiplyCommand, and DivideCommand

from source.calculator import Calculator
from source.calculator_commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

def test_add_command():
    # Test the execute method of the AddCommand class
    calculator = Calculator()
    add_command = AddCommand(calculator)
    assert add_command.execute(2, 3) == 5

def test_subtract_command():
    # Test the execute method of the SubtractCommand class
    calculator = Calculator()
    subtract_command = SubtractCommand(calculator)
    assert subtract_command.execute(5, 3) == 2

def test_multiply_command():
    # Test the execute method of the MultiplyCommand class
    calculator = Calculator()
    multiply_command = MultiplyCommand(calculator)
    assert multiply_command.execute(4, 2) == 8

def test_divide_command():
    # Test the execute method of the DivideCommand class
    calculator = Calculator()
    divide_command = DivideCommand(calculator)
    assert divide_command.execute(6, 3) == 2
