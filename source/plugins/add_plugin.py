# This module defines the AddPlugin class for performing addition in the calculator application


from source.plugin_interface import Plugin
from source.calculator import Calculator

class AddPlugin(Plugin):
    # A plugin class that performs addition for the calculator application
    def __init__(self, calculator: Calculator):
        self.calculator = calculator

    def execute(self, a: float, b: float, *args) -> float:
        return self.calculator.add(a, b)
    
    def get_description(self):
        # Returns a description of the plugin's purpose
        return "This plugin performs addition."
