# app/__init__.py
from app.commands import CommandHandler
from app.commands.add.add_command import AddCommand
from app.commands.subtract.subtract_command import SubtractCommand
from app.commands.multiply.multiply_command import MultiplyCommand
from app.commands.divide.divide_command import DivideCommand
from app.commands.menu.menu_command import MenuCommand
from app.commands.exit.exit_command import ExitCommand

class App:
    def __init__(self):
        self.command_handler = CommandHandler()

    def start(self):
        # Register arithmetic commands
        self.command_handler.register_command("add", AddCommand())
        self.command_handler.register_command("subtract", SubtractCommand())
        self.command_handler.register_command("multiply", MultiplyCommand())
        self.command_handler.register_command("divide", DivideCommand())
        # Register additional commands
        self.command_handler.register_command("menu", MenuCommand())
        self.command_handler.register_command("exit", ExitCommand())

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
