# app/commands/history/history_load_command.py
import logging
from app.commands import Command
from calculator.history_facade import HistoryFacade

COMMAND_NAME = "history_load"

class HistoryLoadCommand(Command):
    def execute(self, args):
        if len(args) != 1:
            print("Usage: history_load <filename>")
            logging.warning("HistoryLoadCommand called with invalid arguments: %s", args)
            return
        filename = args[0]
        try:
            output = HistoryFacade().load_history(filename)
            print(output)
            logging.info("History loaded successfully.")
        except Exception as e:
            logging.exception("Failed to load history:")
            print(f"Error loading history: {e}")
