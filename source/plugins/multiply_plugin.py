# This module defines the MultiplyPlugin class for performing multiplication in the calculator application

from source.plugin_interface import Plugin
from source.calculator import Calculator

class MultiplyPlugin(Plugin):
    # A plugin class that performs multiplication for the calculator application
    def __init__(self, calculator: Calculator):
        self.calculator = calculator

    def execute(self, a: float, b: float, *args) -> float:
        return self.calculator.multiply(a, b)

    def get_description(self):
        # Returns a description of the plugin's purpose
        return "This plugin performs multiplication."
