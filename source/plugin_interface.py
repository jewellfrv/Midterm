# This module defines the Plugin interface for the calculator application.
# It provides the structure for all plugin implementations.



class Plugin:
    # Abstract base class for all plugins in the calculator application
    def execute(self, *args):
        """Execute the plugin command."""
        raise NotImplementedError("This method should be overridden.")
    
    def describe(self):
        # Describe the plugin's functionality
        return "This is a plugin interface for the calculator application."
