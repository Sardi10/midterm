# app/commands/plugin_loader.py
import os
import importlib
from app.commands import Command

def load_plugins():
    """
    Dynamically loads command plugins from subdirectories of app/commands.
    Returns a dictionary mapping command names to command instances.
    """
    plugins = {}
    commands_dir = os.path.dirname(__file__)
    
    for item in os.listdir(commands_dir):
        item_path = os.path.join(commands_dir, item)
        if os.path.isdir(item_path) and os.path.exists(os.path.join(item_path, '__init__.py')):
            for file in os.listdir(item_path):
                if file.endswith('_command.py'):
                    module_name = f"app.commands.{item}.{file[:-3]}"
                    module = importlib.import_module(module_name)
                    # Determine the command name: use module-level variable COMMAND_NAME if it exists, otherwise use the directory name
                    cmd_name = getattr(module, "COMMAND_NAME", item)
                    for attr in dir(module):
                        obj = getattr(module, attr)
                        if isinstance(obj, type) and issubclass(obj, Command) and obj != Command:
                            plugins[cmd_name] = obj()
    return plugins
