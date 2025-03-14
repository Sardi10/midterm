# calculator/history_facade.py
from calculator.history_manager import HistoryManager

class HistoryFacade:
    """
    A Facade for HistoryManager that provides a simplified interface for
    common history operations.
    """
    def __init__(self):
        self.history_manager = HistoryManager()

    def show_history(self):
        if self.history_manager.history_df.empty:
            return "No history available."
        return self.history_manager.history_df.to_string(index=False)

    def save_history(self, filename: str):
        self.history_manager.save_history(filename)
        return f"History saved to {filename}."

    def load_history(self, filename: str):
        self.history_manager.load_history(filename)
        return f"History loaded from {filename}."

    def clear_history(self):
        self.history_manager.clear_history()
        return "History cleared."
