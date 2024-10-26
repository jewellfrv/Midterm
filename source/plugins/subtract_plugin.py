# This module defines the SubtractPlugin class for performing subtraction in the calculator application

from source.plugin_interface import Plugin
from source.calculator import Calculator

class SubtractPlugin(Plugin):
    # A plugin class that performs subtraction for the calculator application
    def __init__(self, calculator: Calculator):
        self.calculator = calculator

    def execute(self, a: float, b: float, *args) -> float:
        return self.calculator.subtract(a, b)

    def get_description(self):
        # Returns a description of the plugin's purpose
        return "This plugin performs division."
