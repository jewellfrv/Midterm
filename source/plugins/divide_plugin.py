# This module defines the DividePlugin class
# Implements division functionality as a plugin for the calculator application.

from source.plugin_interface import Plugin
from source.calculator import Calculator

class DividePlugin(Plugin):
    # A plugin that performs division operation for the calculator application
    def __init__(self, calculator: Calculator):
        self.calculator = calculator

    def execute(self, a: float, b: float, *args) -> float:
        return self.calculator.divide(a, b)

    def get_description(self):
        # Returns a description of the plugin's purpose
        return "This plugin performs division."
