# app/commands/history/history_clear_command.py
import logging
from app.commands import Command
from calculator.history_manager import HistoryManager

COMMAND_NAME = "history_clear"

class HistoryClearCommand(Command):
    def execute(self, args):
        HistoryManager().clear_history()
        print("History cleared.")
