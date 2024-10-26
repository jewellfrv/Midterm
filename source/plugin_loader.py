# This module handles the dynamic loading of plugins for the calculator application
import importlib
import logging
import os
from source import plugin_interface
from source.plugin_interface import Plugin

class PluginLoader:
    # This class dynamically loads plugins for the calculator application
    def __init__(self, plugin_folder='source/plugins'):
        self.plugin_folder = plugin_folder

    def load_plugins(self, plugin_names):
        # Loads plugins based on a list of plugin module names.
        # :param plugin_names: List of plugin module names to load
        for plugin_name in plugin_names:
            try:
                module = importlib.import_module(f"source.plugins.{plugin_name}")
                plugin_class = getattr(module, plugin_name.capitalize())
                plugin_instance = plugin_class()
                
                if isinstance(plugin_instance, plugin_interface):
                    self.plugins[plugin_name] = plugin_instance
                    logging.info(f"Plugin '{plugin_name}' loaded successfully.")
                else:
                    logging.error(f"Plugin '{plugin_name}' does not implement PluginInterface.")
            except (ModuleNotFoundError, AttributeError) as e:
                logging.error(f"Failed to load plugin '{plugin_name}': {e}")

    def list_plugins(self):
        # Lists all currently loaded plugins.
        # :return: A list of plugin names
        if not self.plugins:
            logging.info("No plugins loaded.")
            return []
        logging.info("Loaded plugins: " + ", ".join(self.plugins.keys()))
        return list(self.plugins.keys())

    def unload_plugin(self, plugin_name):
        # Unloads a specific plugin by its name.
        # :param plugin_name: Name of the plugin to unload
        # :return: True if successfully unloaded, False if the plugin was not found
        if plugin_name in self.plugins:
            del self.plugins[plugin_name]
            logging.info(f"Plugin '{plugin_name}' unloaded successfully.")
            return True
        else:
            logging.warning(f"Plugin '{plugin_name}' not found.")
            return False

    def validate_plugins(self):
        # Validates all currently loaded plugins to ensure they conform to the required interface.
        # :return: True if all plugins are valid, False otherwise
        if not self.plugins:
            logging.info("No plugins loaded to validate.")
            return False

        for name, plugin in self.plugins.items():
            if not hasattr(plugin, "execute"):
                logging.error(f"Plugin '{name}' does not have an 'execute' method.")
                return False

        logging.info("All plugins validated successfully.")
        return True
    