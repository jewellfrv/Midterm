# source/plugins/divide_plugin.py
from source.plugin_interface import Plugin
from source.calculator import Calculator

class DividePlugin(Plugin):
    def __init__(self, calculator: Calculator):
        self.calculator = calculator

    def execute(self, a: float, b: float) -> float:
        return self.calculator.divide(a, b)
