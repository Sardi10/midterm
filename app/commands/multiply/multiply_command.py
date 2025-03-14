import logging
from app.commands import Command
from calculator.calculation import Calculation
from calculator.history_manager import HistoryManager

class MultiplyCommand(Command):
    def execute(self, args):
        if len(args) != 2:
            print("Usage: multiply <a> <b>")
            logging.warning("MultiplyCommand called with invalid arguments: %s", args)
            return
        try:
            a = float(args[0])
            b = float(args[1])
            calc = Calculation(a, b, '*')
            calc.perform()
            HistoryManager().add_calculation(calc)
            #result = Calculator.multiply(a, b)
            logging.info("MultiplyCommand executed with a=%s, b=%s, result=%s", a, b, calc.result)
            print(f"The result of {int(a)} multiply {int(b)} is equal to {calc.result}")
        except ValueError:
            logging.exception("Invalid input for MultiplyCommand: %s", args)
            print(f"Invalid number input: {args[0]} or {args[1]} is not a valid number.")
