# tests/test_app.py
import pytest
from app import App
from app.commands.exit.exit_command import ExitCommand

def test_app_start_exit_command(capfd, monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert e.type == SystemExit
    
def test_exit_command_unexpected_arguments(capfd, caplog):
    command = ExitCommand()
    # Call the command with unexpected arguments
    with pytest.raises(SystemExit) as excinfo:
        command.execute(["unexpected_arg"])
    
    # Capture printed output
    out, err = capfd.readouterr()
    # Check that the output contains the expected message
    assert "Exiting..." in out
    
    # Check that a warning about unexpected arguments was logged
    warning_logged = any("ExitCommand received unexpected arguments:" in record.message for record in caplog.records)
    assert warning_logged, "Expected a warning log for unexpected arguments, but none was found."
    
    # Check that the exit message is as expected
    assert excinfo.value.code == "Exiting..."

def test_app_start_unknown_command(capfd, monkeypatch):
    """Test handling of an unknown command before exiting."""
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit):
        app.start()
    captured = capfd.readouterr()
    assert "No such command: unknown_command" in captured.out

def test_menu_command(capfd, monkeypatch):
    # Simulate user typing 'menu' then 'exit'
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Expect the program to exit on 'exit'
    with pytest.raises(SystemExit):
        my_app = App()
        my_app.start()

    # Capture all printed output
    out, err = capfd.readouterr()

    # Verify that the "menu" command actually printed something
    # Adjust this string to match exactly what your menu_command.py prints
    assert "Available commands: add, subtract, multiply, divide, menu, exit" in out
    assert "Commands should be in this format: add 5 3" in out

def test_empty_input_triggers_continue(monkeypatch, capfd):
    # Create an iterator that returns an empty string first, then "exit"
    inputs = iter(["", "exit"])
    monkeypatch.setattr('builtins.input', lambda prompt="": next(inputs))
    
    # Expect that eventually the app will exit when "exit" is encountered
    with pytest.raises(SystemExit):
        App().start()
    
    # Optionally, capture output to verify behavior
    out, err = capfd.readouterr()
    # You could assert that the REPL prompt was shown at least once, but the main point is
    # that the empty input branch (continue) was executed.
