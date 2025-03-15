"""Module providing a function python version."""
# tests/test_history_manager.py
import os
import pandas as pd
import pytest
from datetime import datetime
from calculator.history_manager import HistoryManager
from calculator.calculation import Calculation

# We'll assume that Calculation.perform() performs the arithmetic operation.
# For operator '+', it will add operand1 and operand2.

@pytest.fixture(autouse=True)
def reset_history_manager():
    """
    Fixture to clear the history before and after each test.
    Since HistoryManager is a singleton, we need to ensure a clean state.
    """
    hm = HistoryManager()
    hm.clear_history()
    yield
    hm.clear_history()

def test_add_calculation():
    hm = HistoryManager()
    # Create a Calculation for addition: 1 + 2 = 3
    calc = Calculation(1, 2, '+')
    hm.add_calculation(calc)
    
    # After adding, the history DataFrame should have one record.
    assert not hm.history_df.empty
    assert hm.history_df.shape[0] == 1
    
    # Verify the last record matches our calculation.
    record = hm.get_last()
    assert record["operand1"] == 1
    assert record["operator"] == '+'
    assert record["operand2"] == 2
    assert record["result"] == 3

def test_get_last_empty():
    hm = HistoryManager()
    with pytest.raises(IndexError) as excinfo:
        hm.get_last()
    assert "No calculations in history" in str(excinfo.value)

def test_clear_history():
    hm = HistoryManager()
    calc = Calculation(1, 2, '+')
    hm.add_calculation(calc)
    # Ensure history has records
    assert not hm.history_df.empty
    hm.clear_history()
    # After clearing, the DataFrame should be empty
    assert hm.history_df.empty

def test_save_and_load_history(tmp_path):
    hm = HistoryManager()
    # Add a calculation: 1 + 2 = 3
    calc = Calculation(1, 2, '+')
    hm.add_calculation(calc)
    
    # Save the history to a temporary file.
    file_path = tmp_path / "history_test.csv"
    hm.save_history(str(file_path))
    
    # Clear history and verify it's empty.
    hm.clear_history()
    assert hm.history_df.empty
    
    # Now load history from the CSV file.
    hm.load_history(str(file_path))
    # The history should be restored.
    assert not hm.history_df.empty
    record = hm.get_last()
    assert record["operand1"] == 1
    assert record["operator"] == '+'
    assert record["operand2"] == 2
    assert record["result"] == 3

def test_delete_history_file(tmp_path):
    hm = HistoryManager()
    # Create a dummy file in the temporary directory.
    file_path = tmp_path / "dummy_history.csv"
    file_path.write_text("dummy data")
    
    # Ensure the file exists.
    assert os.path.exists(str(file_path))
    
    # Use delete_history_file to remove it.
    hm.delete_history_file(str(file_path))
    
    # Verify the file has been deleted.
    assert not os.path.exists(str(file_path))
