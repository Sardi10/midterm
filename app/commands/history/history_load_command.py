# app/commands/history/history_load_command.py
import logging
from app.commands import Command
from calculator.history_manager import HistoryManager

COMMAND_NAME = "history_load"

class HistoryLoadCommand(Command):
    def execute(self, args):
        if len(args) != 1:
            print("Usage: history_load <filename>")
            logging.warning("HistoryLoadCommand called with invalid arguments: %s", args)
            return
        filename = args[0]
        try:
            HistoryManager().load_history(filename)
            print(f"History loaded from {filename}.")
        except Exception as e:
            logging.exception("Failed to load history:")
            print(f"Error loading history: {e}")
