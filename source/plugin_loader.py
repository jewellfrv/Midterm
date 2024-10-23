# source/plugin_loader.py
import importlib
import os
from source.plugin_interface import Plugin

class PluginLoader:
    def __init__(self, plugin_folder='src/plugins'):
        self.plugin_folder = plugin_folder

    def load_plugins(self):
        plugins = {}
        for filename in os.listdir(self.plugin_folder):
            if filename.endswith('_plugin.py') and filename != '__init__.py':
                module_name = filename[:-3]  # Remove the .py extension
                module = importlib.import_module(f"src.plugins.{module_name}")
                # Create an instance of the plugin class
                class_name = module_name.capitalize() + "Plugin"
                plugin_class = getattr(module, class_name)
                plugins[module_name] = plugin_class
        return plugins
