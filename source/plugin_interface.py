# source/plugin_interface.py

class Plugin:
    def execute(self, *args):
        """Execute the plugin command."""
        raise NotImplementedError("This method should be overridden.")
