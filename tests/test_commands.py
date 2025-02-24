# tests/test_commands.py
import pytest
from app.commands import CommandHandler, Command
from app.commands.add.add_command import AddCommand
from app.commands.subtract.subtract_command import SubtractCommand
from app.commands.multiply.multiply_command import MultiplyCommand
from app.commands.divide.divide_command import DivideCommand

def test_add_command(capfd):
    command = AddCommand()
    command.execute(["5", "3"])
    out, _ = capfd.readouterr()
    assert out == "The result of 5 add 3 is equal to 8.0\n"

def test_subtract_command(capfd):
    command = SubtractCommand()
    command.execute(["10", "2"])
    out, _ = capfd.readouterr()
    assert out == "The result of 10 subtract 2 is equal to 8.0\n"

def test_multiply_command(capfd):
    command = MultiplyCommand()
    command.execute(["4", "5"])
    out, _ = capfd.readouterr()
    assert out == "The result of 4 multiply 5 is equal to 20.0\n"

def test_divide_command(capfd):
    command = DivideCommand()
    command.execute(["20", "4"])
    out, _ = capfd.readouterr()
    assert out == "The result of 20 divide 4 is equal to 5.0\n"

# Define a dummy command that implements the Command interface
class DummyCommand(Command):
    def execute(self, args):
        super().execute(args)
        print("Dummy executed")

def test_execute_command_success(capfd):
    """Test that a registered command is executed successfully."""
    handler = CommandHandler()
    handler.register_command("dummy", DummyCommand())
    handler.execute_command("dummy")
    out, _ = capfd.readouterr()
    # Check that the dummy command's output is printed
    assert "Dummy executed" in out

def test_execute_command_keyerror(capfd):
    """Test that calling an unregistered command prints the error message."""
    handler = CommandHandler()
    # Do not register any command, so "nonexistent" will trigger KeyError
    handler.execute_command("nonexistent")
    out, _ = capfd.readouterr()
    # Verify that the except block's print statement was executed
    assert "No such command: nonexistent" in out

def test_add_command_length(capfd):
    command = AddCommand()
    command.execute(["5"])
    out, _ = capfd.readouterr()
    assert out == "Usage: add <a> <b>\n"

def test_add_command_invalid_argument(capfd):
    command = AddCommand()
    command.execute(["5","b"])
    out, _ = capfd.readouterr()
    assert out == "Invalid number input: 5 or b is not a valid number.\n"

def test_devide_command_length(capfd):
    command = DivideCommand()
    command.execute(["5"])
    out, _ = capfd.readouterr()
    assert out == "Usage: divide <a> <b>\n"

def test_divide_command_invalid_argument_1(capfd):
    command = DivideCommand()
    command.execute(["5","b"])
    out, _ = capfd.readouterr()
    assert out == "Invalid number input: 5 or b is not a valid number.\n"

def test_add_command_invalid_argument_2(capfd):
    command = DivideCommand()
    command.execute(["5","0"])
    out, _ = capfd.readouterr()
    assert out == "An error occurred: Cannot divide by zero.\n"

def test_multiply_command_length(capfd):
    command = MultiplyCommand()
    command.execute(["5"])
    out, _ = capfd.readouterr()
    assert out == "Usage: multiply <a> <b>\n"

def test_multiply_command_invalid(capfd):
    command = MultiplyCommand()
    command.execute(["5","b"])
    out, _ = capfd.readouterr()
    assert out == "Invalid number input: 5 or b is not a valid number.\n"

def test_subtract_command_length(capfd):
    command = SubtractCommand()
    command.execute(["5"])
    out, _ = capfd.readouterr()
    assert out == "Usage: subtract <a> <b>\n"

def test_subtract_command_invalid(capfd):
    command = SubtractCommand()
    command.execute(["5","b"])
    out, _ = capfd.readouterr()
    assert out == "Invalid number input: 5 or b is not a valid number.\n"
