# src/main.py
from calculator import Calculator
from calculator_commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

def repl():
    calculator = Calculator()
    commands = {
        'add': AddCommand(calculator),
        'subtract': SubtractCommand(calculator),
        'multiply': MultiplyCommand(calculator),
        'divide': DivideCommand(calculator),
    }
    
    print("Welcome! Type 'exit' to quit.")
    while True:
        command_input = input(">>> ").strip().lower()
        if command_input == "exit":
            print("Goodbye!")
            break
        elif command_input.startswith("add "):
            _, a, b = command_input.split()
            result = commands['add'].execute(float(a), float(b))
            print(f"Result: {result}")
        elif command_input.startswith("subtract "):
            _, a, b = command_input.split()
            result = commands['subtract'].execute(float(a), float(b))
            print(f"Result: {result}")
        elif command_input.startswith("multiply "):
            _, a, b = command_input.split()
            result = commands['multiply'].execute(float(a), float(b))
            print(f"Result: {result}")
        elif command_input.startswith("divide "):
            _, a, b = command_input.split()
            try:
                result = commands['divide'].execute(float(a), float(b))
                print(f"Result: {result}")
            except ValueError as e:
                print(e)
        else:
            print(f"Command '{command_input}' is not recognized yet.")
