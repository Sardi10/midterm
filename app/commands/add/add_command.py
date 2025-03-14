# app/commands/add/add_command.py
import logging
from app.commands import Command
from calculator.calculation import Calculation
from calculator.history_manager import HistoryManager

class AddCommand(Command):
    def execute(self, args):
        if len(args) != 2:
            print("Usage: add <a> <b>")
            logging.warning("Add command called with invalid number of arguments: %s", args)
            return
        try:
            a = float(args[0])
            b = float(args[1])

            # Create a Calculation object for addition
            calc = Calculation(a, b, '+')
            calc.perform()

            # Store the Calculation in the Pandas-based history
            HistoryManager().add_calculation(calc)

            logging.info("AddCommand executed with a=%s, b=%s. Result: %s", a, b, calc.result)
            print(f"The result of {int(a)} add {int(b)} is equal to {calc.result}")
        except ValueError:
            logging.exception("Invalid input for AddCommand: %s", args)
            print(f"Invalid number input: {args[0]} or {args[1]} is not a valid number.")
