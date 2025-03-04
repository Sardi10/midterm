# app/commands/exit/exit_command.py
import logging
from app.commands import Command
import sys

class ExitCommand(Command):
    def execute(self, args):
        if args:
            logging.warning("ExitCommand received unexpected arguments: %s", args)
        logging.info("ExitCommand executed. Exiting application.")
        print("Exiting...")
        sys.exit("Exiting...")
