# This module defines various command classes for calculator operations, including Add, Subtract, Multiply, and Divide.
# Each class implements the execute method to perform the corresponding arithmetic operation.

from .commands import Command
from .calculator import Calculator

class AddCommand(Command):
    # Command to perform addition
    def __init__(self, calculator: Calculator):
        self.calculator = calculator

    def execute(self, a: float, b: float, *args) -> float:
        return self.calculator.add(a, b)
   
    def description(self):
        return "Adds two numbers"

class SubtractCommand(Command):
    # Command to perform subtraction
    def __init__(self, calculator: Calculator):
        self.calculator = calculator

    def execute(self, a: float, b: float, *args) -> float:
        return self.calculator.subtract(a, b)
    
    def description(self):
        return "Subtracts two numbers"

class MultiplyCommand(Command):
    # Command to perform multiplication
    def __init__(self, calculator: Calculator):
        self.calculator = calculator

    def execute(self, a: float, b: float, *args) -> float:
        return self.calculator.multiply(a, b)
    
    def description(self):
        return "Multiplies two numbers"

class DivideCommand(Command):
    # Command to perform division
    def __init__(self, calculator: Calculator):
        self.calculator = calculator

    def execute(self, a: float, b: float, *args) -> float:
        return self.calculator.divide(a, b)
    
    def description(self):
        return "Divides two numbers"
    