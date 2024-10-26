# Tests for plugin classes including AddPlugin, SubtractPlugin, MultiplyPlugin, and DividePlugin

from source.calculator import Calculator
from source.plugins.add_plugin import AddPlugin
from source.plugins.subtract_plugin import SubtractPlugin
from source.plugins.multiply_plugin import MultiplyPlugin
from source.plugins.divide_plugin import DividePlugin

def test_add_plugin():
    # Test the addition operation using the AddPlugin class
    calculator = Calculator()
    add_plugin = AddPlugin(calculator)
    assert add_plugin.execute(3, 2) == 5

def test_subtract_plugin():
    # Test the subtraction operation using the SubtractPlugin class
    calculator = Calculator()
    subtract_plugin = SubtractPlugin(calculator)
    assert subtract_plugin.execute(5, 3) == 2

def test_multiply_plugin():
    # Test the multiplication operation using the MultiplyPlugin class
    calculator = Calculator()
    multiply_plugin = MultiplyPlugin(calculator)
    assert multiply_plugin.execute(4, 2) == 8

def test_divide_plugin():
    # Test the division operation using the DividePlugin class
    calculator = Calculator()
    divide_plugin = DividePlugin(calculator)
    assert divide_plugin.execute(6, 3) == 2
