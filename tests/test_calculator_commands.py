# tests/test_calculator_commands.py
from source.calculator import Calculator
from source.calculator_commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

def test_add_command():
    calculator = Calculator()
    add_command = AddCommand(calculator)
    assert add_command.execute(2, 3) == 5

def test_subtract_command():
    calculator = Calculator()
    subtract_command = SubtractCommand(calculator)
    assert subtract_command.execute(5, 3) == 2

def test_multiply_command():
    calculator = Calculator()
    multiply_command = MultiplyCommand(calculator)
    assert multiply_command.execute(4, 2) == 8

def test_divide_command():
    calculator = Calculator()
    divide_command = DivideCommand(calculator)
    assert divide_command.execute(6, 3) == 2
