# app/commands/history/history_clear_command.py
import logging
from app.commands import Command
from calculator.history_facade import HistoryFacade

COMMAND_NAME = "history_clear"

class HistoryClearCommand(Command):
    def execute(self, args):
        try:
            output = HistoryFacade().clear_history()
            print(output)
            logging.info("History cleared successfully.")
        except Exception as e:
            logging.exception("Failed to clear history:")
            print(f"Error clearing history: {e}")
