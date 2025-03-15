# app/commands/menu/menu_command.py
from app.commands import Command
import logging

class MenuCommand(Command):
    def execute(self, args):
        logging.info("Displaying menu options.")
        print("Available commands: add, subtract, multiply, divide, menu, exit\n")
        print("History Commands: history_show, histor_clear, history_load, history_save\n")
        print("Commands should be in this format: add 5 3\n")
