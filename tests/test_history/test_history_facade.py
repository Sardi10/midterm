"""Module providing a function python version."""
# tests/test_history_facade.py
import pandas as pd
from calculator.history_facade import HistoryFacade

def test_show_history_empty():
    """
    Test that show_history() returns "No history available."
    when the history DataFrame is empty.
    """
    facade = HistoryFacade()
    # Ensure the history is empty by setting it to an empty DataFrame
    facade.history_manager.history_df = pd.DataFrame(
        columns=["timestamp", "operand1", "operator", "operand2", "result"]
    )
    output = facade.show_history()
    assert output == "No history available."

def test_show_history_non_empty():
    """
    Test that show_history() returns a string representation
    of the DataFrame when it is not empty.
    """
    facade = HistoryFacade()
    # Create a DataFrame with a sample record
    data = {
       "timestamp": ["2025-03-07 12:00:00"],
       "operand1": [1.0],
       "operator": ["+"],
       "operand2": [2.0],
       "result": [3.0]
    }
    df = pd.DataFrame(data)
    facade.history_manager.history_df = df
    expected_output = df.to_string(index=False)
    assert facade.show_history() == expected_output

def test_save_history(monkeypatch):
    """
    Test that save_history() returns the correct success message.
    The actual save operation is overridden to avoid file I/O.
    """
    facade = HistoryFacade()

    # Override the save_history method on the history_manager to do nothing.
    def fake_save_history(filename):
        _ = filename
    monkeypatch.setattr(facade.history_manager, "save_history", fake_save_history)

    filename = "test.csv"
    result = facade.save_history(filename)
    assert result == f"History saved to {filename}."

def test_load_history(monkeypatch):
    """
    Test that load_history() returns the correct success message.
    The actual load operation is overridden to avoid file I/O.
    """
    facade = HistoryFacade()

    # Override the load_history method on the history_manager to do nothing.
    def fake_load_history(filename):
        _ = filename
    monkeypatch.setattr(facade.history_manager, "load_history", fake_load_history)

    filename = "test.csv"
    result = facade.load_history(filename)
    assert result == f"History loaded from {filename}."

def test_clear_history(monkeypatch):
    """
    Test that clear_history() returns the correct success message.
    The actual clear operation is overridden.
    """
    facade = HistoryFacade()

    def fake_clear_history():
        pass
    monkeypatch.setattr(facade.history_manager, "clear_history", fake_clear_history)

    result = facade.clear_history()
    assert result == "History cleared."
