# This module contains the Calculator class that performs basic arithmetic operations.
# It supports addition, subtraction, multiplication, and division.

import logging

class Calculator:
    # A simple calculator class to perform basic arithmetic operations.
    def add(self, a: float, b: float) -> float:
        return a + b
        # Adds two numbers using specified parameters and returns result

    def subtract(self, a: float, b: float) -> float:
        return a - b
        # Subtracts two numbers using specified parameters and returns result

    def multiply(self, a: float, b: float) -> float:
        return a * b
        # Multiplies two numbers using specified parameters and returns result

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            logging.error("Division by zero attempted")
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
        # Divides two numbers using specified parameters and returns result
        # Raises ZeroDivisonError if division by zero is attempted
    