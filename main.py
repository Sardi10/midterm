# main.py
import os
import sys
import logging
from dotenv import load_dotenv

from app import App
from calculator.calculator import Calculator
from calculator.calculation import Calculation

# 1. Load environment variables from the .env file
load_dotenv()

# 2. Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]  # Logs to console
)

def parse_args(args):
    """
    Parses the command-line arguments.
    Expected arguments: a, b, operation
    Returns a tuple (a, b, operation) with a and b as floats if valid.
    """
    if len(args) != 3:
        raise ValueError("Please provide exactly three arguments: a, b, and operation.")

    a_str, b_str, operation = args

    try:
        a = float(a_str)
        b = float(b_str)
    except ValueError:
        raise ValueError(f"Invalid number input: {a_str} or {b_str} is not a valid number.")
    
    return a, b, operation

def perform_operation(a, b, operation):
    """
    Maps the operation string to the corresponding Calculator method.
    """
    if operation == 'add':
        return Calculator.add(a, b)
    elif operation == 'subtract':
        return Calculator.subtract(a, b)
    elif operation == 'multiply':
        return Calculator.multiply(a, b)
    elif operation == 'divide':
        try:
            return Calculator.divide(a, b)
        except ZeroDivisionError:
            raise ZeroDivisionError("Cannot divide by zero.")
    else:
        raise ValueError(f"Unknown operation: {operation}")

def one_shot_mode():
    """
    Runs a single calculation based on command-line arguments.
    """
    try:
        a, b, operation = parse_args(sys.argv[1:])
        result = perform_operation(a, b, operation)
        msg = f"The result of {int(a)} {operation} {int(b)} is equal to {result}"
        logging.info(msg)
        print(msg)
    except Exception as e:
        logging.exception("An error occurred in one-shot mode:")
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # 3. Log the current environment mode (default to 'production' if not set)
    app_env = os.getenv("APP_ENV", "production")
    logging.info(f"Running in {app_env} mode.")

    # 4. Decide which mode to run:
    #    - If there are command-line arguments (beyond the script name), use one_shot_mode().
    #    - Otherwise, start the interactive REPL by creating an App instance.
    if len(sys.argv) > 1:
        one_shot_mode()
    else:
        logging.info("Starting interactive mode...")
        app = App()
        app.start()
