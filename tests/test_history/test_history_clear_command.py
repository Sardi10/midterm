"""Module providing a function python version."""
# tests/test_history_clear_command.py
import pytest
from app.commands.history.history_clear_command import HistoryClearCommand

def test_history_clear_command_success(capfd, caplog):
    """
    Test that HistoryClearCommand executes successfully when no error occurs.
    It should print "History cleared." and log an info message.
    """
    # Set caplog to capture INFO-level logs
    caplog.set_level("INFO")
    
    command = HistoryClearCommand()
    # Execute the command with no arguments
    command.execute([])
    
    # Capture printed output
    out, _ = capfd.readouterr()
    assert "History cleared." in out, f"Expected output 'History cleared.' not found; got: {out}"
    
    # Verify that an info log was generated
    info_logged = any("History cleared successfully." in record.message for record in caplog.records)
    assert info_logged, "Expected log message 'History cleared successfully.' not found."

def test_history_clear_command_failure(monkeypatch, capfd, caplog):
    """
    Test that HistoryClearCommand handles exceptions correctly.
    We simulate an error by monkeypatching HistoryFacade.clear_history to raise an exception.
    """
    # Define a fake clear_history method that always raises an exception
    def fake_clear_history(self):
        raise Exception("Test Exception")
    
    # Monkeypatch the clear_history method in HistoryFacade
    monkeypatch.setattr("calculator.history_facade.HistoryFacade.clear_history", fake_clear_history)
    
    command = HistoryClearCommand()
    command.execute([])
    
    # Capture printed output
    out, _ = capfd.readouterr()
    assert "Error clearing history: Test Exception" in out, "Expected error message not printed."
    
    # Verify that an exception log was generated
    error_logged = any("Failed to clear history:" in record.message for record in caplog.records)
    assert error_logged, "Expected exception log not found."
