# app/commands/history/history_save_command.py
import logging
from app.commands import Command
from calculator.history_manager import HistoryManager

COMMAND_NAME = "history_save"

class HistorySaveCommand(Command):
    def execute(self, args):
        if len(args) != 1:
            print("Usage: history_save <filename>")
            logging.warning("HistorySaveCommand called with invalid arguments: %s", args)
            return
        filename = args[0]
        try:
            HistoryManager().save_history(filename)
            print(f"History saved to {filename}.")
        except Exception as e:
            logging.exception("Failed to save history:")
            print(f"Error saving history: {e}")
