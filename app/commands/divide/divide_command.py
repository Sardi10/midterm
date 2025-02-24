# app/commands/divide/divide_command.py
from app.commands import Command
from calculator.calculator import Calculator

class DivideCommand(Command):
    def execute(self, args):
        if len(args) != 2:
            print("Usage: divide <a> <b>")
            return
        try:
            a = float(args[0])
            b = float(args[1])
            result = Calculator.divide(a, b)
            print(f"The result of {int(a)} divide {int(b)} is equal to {result}")
        except ValueError:
            print(f"Invalid number input: {args[0]} or {args[1]} is not a valid number.")
        except ZeroDivisionError:
            print("An error occurred: Cannot divide by zero.")
