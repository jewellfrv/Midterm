# source/main.py
from calculator import Calculator
from plugin_loader import PluginLoader

def repl():
    calculator = Calculator()
    plugin_loader = PluginLoader()
    loaded_plugins = plugin_loader.load_plugins()
    
    # Instantiate plugins and store command references
    commands = {}
    for name, plugin_cls in loaded_plugins.items():
        commands[name] = plugin_cls(calculator)

    print("Welcome! Type 'exit' to quit.")
    print("Available commands: add, subtract, multiply, divide")
    
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
