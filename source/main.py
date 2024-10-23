def repl():
    print("Welcome! Type 'exit' to quit.")
    while True:
        command = input(">>> ").strip().lower()
        if command == "exit":
            print("Goodbye!")
            break
        else:
            print(f"Command '{command}' is not recognized yet.")

if __name__ == "__main__":
    repl()
