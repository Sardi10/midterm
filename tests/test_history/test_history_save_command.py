# tests/test_history_save_command.py
import pytest
from app.commands.history.history_save_command import HistorySaveCommand

def test_history_save_command_success(monkeypatch, capfd, caplog):
    """
    Test that HistorySaveCommand executes successfully when provided with a valid filename.
    It should print the success message and log an info message.
    """
    caplog.set_level("INFO")
    
    # Override HistoryFacade.save_history to simulate a successful save
    def fake_save_history(self, filename):
        return f"History saved to {filename}."
    
    monkeypatch.setattr("calculator.history_facade.HistoryFacade.save_history", fake_save_history)
    
    command = HistorySaveCommand()
    command.execute(["test.csv"])
    
    # Capture printed output
    out, _ = capfd.readouterr()
    assert "History saved to test.csv." in out, f"Expected success message not found; got: {out}"
    
    # Verify that an info log was generated
    info_logged = any("History saved successfully." in record.message for record in caplog.records)
    assert info_logged, "Expected info log message 'History saved successfully.' not found."

def test_history_save_command_invalid_arguments(capfd, caplog):
    """
    Test that HistorySaveCommand handles invalid arguments correctly.
    It should print the usage message and log a warning when no filename is provided.
    """
    caplog.set_level("WARNING")
    
    command = HistorySaveCommand()
    command.execute([])  # No arguments provided
    
    out, _ = capfd.readouterr()
    assert "Usage: history_save <filename>" in out, f"Expected usage message not found; got: {out}"
    
    warning_logged = any("HistorySaveCommand called with invalid arguments:" in record.message for record in caplog.records)
    assert warning_logged, "Expected warning log for invalid arguments not found."

def test_history_save_command_failure(monkeypatch, capfd, caplog):
    """
    Test that HistorySaveCommand handles exceptions correctly.
    Simulate a failure by making HistoryFacade.save_history raise an exception.
    """
    caplog.set_level("ERROR")
    
    def fake_save_history(self, filename):
        raise Exception("Test save error")
    
    monkeypatch.setattr("calculator.history_facade.HistoryFacade.save_history", fake_save_history)
    
    command = HistorySaveCommand()
    command.execute(["test.csv"])
    
    out, _ = capfd.readouterr()
    assert "Error saving history: Test save error" in out, f"Expected error message not found; got: {out}"
    
    error_logged = any("Failed to save history:" in record.message for record in caplog.records)
    assert error_logged, "Expected error log for failed save not found."
