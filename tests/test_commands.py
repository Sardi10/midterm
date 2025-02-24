# tests/test_commands.py
import pytest
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
