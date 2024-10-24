# source/calculator_commands.py
from .commands import Command
from .calculator import Calculator

class AddCommand(Command):
    def __init__(self, calculator: Calculator):
        self.calculator = calculator

    def execute(self, a: float, b: float) -> float:
        return self.calculator.add(a, b)

class SubtractCommand(Command):
    def __init__(self, calculator: Calculator):
        self.calculator = calculator

    def execute(self, a: float, b: float) -> float:
        return self.calculator.subtract(a, b)

class MultiplyCommand(Command):
    def __init__(self, calculator: Calculator):
        self.calculator = calculator

    def execute(self, a: float, b: float) -> float:
        return self.calculator.multiply(a, b)

class DivideCommand(Command):
    def __init__(self, calculator: Calculator):
        self.calculator = calculator

    def execute(self, a: float, b: float) -> float:
        return self.calculator.divide(a, b)
