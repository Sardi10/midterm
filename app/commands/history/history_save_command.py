# app/commands/history/history_save_command.py
import logging
from app.commands import Command
from calculator.history_facade import HistoryFacade

COMMAND_NAME = "history_save"

class HistorySaveCommand(Command):
    def execute(self, args):
        if len(args) != 1:
            print("Usage: history_save <filename>")
            logging.warning("HistorySaveCommand called with invalid arguments: %s", args)
            return
        filename = args[0]
        try:
            output = HistoryFacade().save_history(filename)
            print(output)
            logging.info("History saved successfully.")
        except Exception as e:
            logging.exception("Failed to save history:")
            print(f"Error saving history: {e}")
