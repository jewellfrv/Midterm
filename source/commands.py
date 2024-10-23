# src/commands.py

class Command:
    def execute(self, *args):
        raise NotImplementedError("This method should be overridden.")
