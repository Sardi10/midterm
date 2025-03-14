# app/__init__.py
from app.commands import CommandHandler
from app.commands.plugin_loader import load_plugins

class App:
    def __init__(self):
        self.command_handler = CommandHandler()

    def start(self):
        # Dynamically load command plugins from app/commands
        plugins = load_plugins()
        for command_name, command_instance in plugins.items():
            self.command_handler.register_command(command_name, command_instance)

        print("Type 'exit' to exit or 'menu' to enter menu section.")
        while True:
            cmd_input = input(">>> ").strip().split()
            if not cmd_input:
                continue
            cmd_name = cmd_input[0].lower()
            args = cmd_input[1:]
            if cmd_name in self.command_handler.commands:
                self.command_handler.commands[cmd_name].execute(args)
            else:
                print(f"No such command: {cmd_name}")
