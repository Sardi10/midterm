# app/commands/menu/menu_command.py
from app.commands import Command

class MenuCommand(Command):
    def execute(self, args):
        print("Available commands: add, subtract, multiply, divide, menu, exit\n")
        print("Commands should be in this format: add 5 3\n")
