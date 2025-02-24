# app/commands/exit/exit_command.py
from app.commands import Command
import sys

class ExitCommand(Command):
    def execute(self, args):
        print("Exiting...")
        sys.exit("Exiting...")
