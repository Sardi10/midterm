import logging
from app.commands import Command
from calculator.history_manager import HistoryManager
from calculator.calculation_factory import CalculationFactory

class AddCommand(Command):
    def execute(self, args):
        if len(args) != 2:
            print("Usage: add <a> <b>")
            logging.warning("Add command called with invalid number of arguments: %s", args)
            return
        try:
            a = float(args[0])
            b = float(args[1])
            # Instead of calling Calculator.add() directly, we'll create a Calculation object
            calc = CalculationFactory.create_calculation(a, b, '+')
            #calc = Calculation(a, b, '+')
            result = calc.perform()

            # NOW we add the Calculation to the history
            HistoryManager().add_calculation(calc)

            logging.info("AddCommand executed with a=%s, b=%s. Result: %s", a, b, result)
            print(f"The result of {int(a)} add {int(b)} is equal to {result}")
        except ValueError:
            logging.exception("Invalid input for AddCommand: %s", args)
            print(f"Invalid number input: {args[0]} or {args[1]} is not a valid number.")
