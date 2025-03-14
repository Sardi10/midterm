from app.commands import Command
from calculator.history_manager import HistoryManager

COMMAND_NAME = "history_show"

class HistoryShowCommand(Command):
    def execute(self, args):
        history_df = HistoryManager().history_df
        if history_df.empty:
            print("No history available.")
        else:
            print(history_df.to_string(index=False))
