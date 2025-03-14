# app/commands/history/history_show_command.py
import logging
from app.commands import Command
from calculator.history_facade import HistoryFacade

COMMAND_NAME = "history_show"

class HistoryShowCommand(Command):
    def execute(self, args):
        try:
            output = HistoryFacade().show_history()
            print(output)
            logging.info("History shown successfully.")
        except Exception as e:
            logging.exception("Failed to show history:")
            print(f"Error showing history: {e}")
