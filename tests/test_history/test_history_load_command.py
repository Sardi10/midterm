"""Module providing a function python version."""
# tests/test_history_load_command.py
from app.commands.history.history_load_command import HistoryLoadCommand

def test_history_load_command_success(monkeypatch, capfd, caplog):
    """
    Test that HistoryLoadCommand executes successfully when a valid filename is provided.
    It should print the success message returned by the facade and log an info message.
    """
    caplog.set_level("INFO")

    # Override HistoryFacade.load_history to simulate a successful load.
    def fake_load_history(self, filename):
        _ = self
        return f"History loaded from {filename}."

    monkeypatch.setattr("calculator.history_facade.HistoryFacade.load_history", fake_load_history)

    command = HistoryLoadCommand()
    command.execute(["test.csv"])

    # Capture printed output
    out, _ = capfd.readouterr()
    assert "History loaded from test.csv." in out, f"Output was: {out}"

    # Verify that an info log was generated.
    info_logged = any("History loaded successfully." in record.message for record in caplog.records)
    assert info_logged, "Expected info log message not found."

def test_history_load_command_invalid_arguments(capfd, caplog):
    """
    Test that HistoryLoadCommand handles invalid arguments.
    When no filename is provided, it should print a usage message and log a warning.
    """
    caplog.set_level("WARNING")

    command = HistoryLoadCommand()
    command.execute([])  # No arguments provided.

    out, _ = capfd.readouterr()
    assert "Usage: history_load <filename>" in out, f"Output was: {out}"

    warning_logged = any("HistoryLoadCommand called with invalid arguments:"
                         in record.message for record in caplog.records)
    assert warning_logged, "Expected warning log message not found."

def test_history_load_command_failure(monkeypatch, capfd, caplog):
    """
    Test that HistoryLoadCommand handles exceptions correctly.
    Simulate an error by monkeypatching HistoryFacade.load_history to raise an exception.
    """
    caplog.set_level("ERROR")

    def fake_load_history(self, filename):
        raise ValueError("Test load error")
    monkeypatch.setattr("calculator.history_facade.HistoryFacade.load_history", fake_load_history)

    command = HistoryLoadCommand()
    command.execute(["test.csv"])

    out, _ = capfd.readouterr()
    assert "Error loading history: Test load error" in out, f"Output was: {out}"

    error_logged = any("Failed to load history:" in record.message for record in caplog.records)
    assert error_logged, "Expected error log message not found."
