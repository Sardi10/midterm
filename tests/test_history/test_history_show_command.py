# tests/test_history_show_command.py
import pytest
from app.commands.history.history_show_command import HistoryShowCommand

def test_history_show_command_success(monkeypatch, capfd, caplog):
    """
    Test that HistoryShowCommand executes successfully.
    It should print the history output and log an info message.
    """
    caplog.set_level("INFO")
    
    # Override HistoryFacade.show_history to simulate a successful output.
    def fake_show_history(self):
        return "Fake history: record1, record2"
    
    monkeypatch.setattr("calculator.history_facade.HistoryFacade.show_history", fake_show_history)
    
    command = HistoryShowCommand()
    command.execute([])
    
    # Capture printed output
    out, _ = capfd.readouterr()
    assert "Fake history: record1, record2" in out, f"Output did not contain expected text; got: {out}"
    
    # Verify that an info log was generated.
    info_logged = any("History shown successfully." in record.message for record in caplog.records)
    assert info_logged, "Expected info log message 'History shown successfully.' not found."

def test_history_show_command_failure(monkeypatch, capfd, caplog):
    """
    Test that HistoryShowCommand handles exceptions properly.
    We simulate an error by monkeypatching HistoryFacade.show_history to raise an exception.
    """
    caplog.set_level("ERROR")
    
    def fake_show_history(self):
        raise Exception("Test show error")
    
    monkeypatch.setattr("calculator.history_facade.HistoryFacade.show_history", fake_show_history)
    
    command = HistoryShowCommand()
    command.execute([])
    
    # Capture printed output
    out, _ = capfd.readouterr()
    assert "Error showing history: Test show error" in out, f"Expected error message not found; got: {out}"
    
    error_logged = any("Failed to show history:" in record.message for record in caplog.records)
    assert error_logged, "Expected error log message for failure not found."
