import logging
from app.commands import Command
from calculator.calculation_factory import CalculationFactory
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
            calc = CalculationFactory.create_calculation(a, b, '*')
            #calc = Calculation(a, b, '*')
            result = calc.perform()

            # NOW we add the Calculation to the history
            HistoryManager().add_calculation(calc)
            # result = Calculator.multiply(a, b)
            logging.info("MultiplyCommand executed with a=%s, b=%s, result=%s", a, b, result)
            print(f"The result of {int(a)} multiply {int(b)} is equal to {result}")
        except ValueError:
            logging.exception("Invalid input for MultiplyCommand: %s", args)
            print(f"Invalid number input: {args[0]} or {args[1]} is not a valid number.")
