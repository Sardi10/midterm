# calculator/history_manager.py
import pandas as pd
from datetime import datetime
from calculator.calculation import Calculation

class HistoryManager:
    """
    Manages calculation history using a Pandas DataFrame.
    Implements a Facade pattern for CSV I/O and history operations.
    This is implemented as a Singleton so that all parts of the app share the same history.
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(HistoryManager, cls).__new__(cls)
            # Initialize an empty DataFrame with designated columns
            cls._instance.history_df = pd.DataFrame(
                columns=["timestamp", "operand1", "operator", "operand2", "result"]
            )
        return cls._instance

    def add_calculation(self, calc: Calculation):
        if calc.result is None:
            calc.perform()

        # Make sure this line exists and is spelled correctly
        new_record = {
            "timestamp": datetime.now(),
            "operand1": calc.operand1,
            "operator": calc.operator,
            "operand2": calc.operand2,
            "result": calc.result
        }

        # Create a one-row DataFrame from new_record
        new_row_df = pd.DataFrame([new_record])
        # Concatenate it to the existing history DataFrame
        self.history_df = pd.concat([self.history_df, new_row_df], ignore_index=True)

    def get_last(self):
        """
        Retrieve the last calculation record as a dictionary.
        """
        if self.history_df.empty:
            raise IndexError("No calculations in history")
        last_record = self.history_df.iloc[-1]
        return last_record.to_dict()

    def clear_history(self):
        """
        Clear all calculation history.
        """
        self.history_df = self.history_df.iloc[0:0]

    def save_history(self, filename: str):
        """
        Save the history DataFrame to a CSV file.
        """
        self.history_df.to_csv(filename, index=False)

    def load_history(self, filename: str):
        """
        Load history from a CSV file.
        """
        self.history_df = pd.read_csv(filename, parse_dates=["timestamp"])

    def delete_history_file(self, filename: str):
        """
        Delete the specified CSV file from disk.
        """
        import os
        if os.path.exists(filename):
            os.remove(filename)
