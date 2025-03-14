import logging
from app.commands import Command
from calculator.calculator import Calculator
from calculator.calculation import Calculation
from calculator.history_manager import HistoryManager

class DivideCommand(Command):
    def execute(self, args):
        if len(args) != 2:
            print("Usage: divide <a> <b>")
            logging.warning("DivideCommand called with invalid arguments: %s", args)
            return
        try:
            a = float(args[0])
            b = float(args[1])
            calc = Calculation(a, b, '/')
            calc.perform()
            HistoryManager().add_calculation(calc)
            #result = Calculator.divide(a, b)
          #  logging.info("DivideCommand executed with a=%s, b=%s, Result=%s", a, b, calc.result)
            print(f"The result of {int(a)} divide {int(b)} is equal to {calc.result}")
        except ValueError:
            logging.exception("Invalid input for DivideCommand: %s", args)
            print(f"Invalid number input: {args[0]} or {args[1]} is not a valid number.")
        except ZeroDivisionError:
            logging.exception("Division by zero error in DivideCommand with args: %s", args)
            print("An error occurred: Cannot divide by zero.")
