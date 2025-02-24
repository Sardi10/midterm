Command Pattern and Plugins Homework 5 Requirements Mapping
============================================================

Requirement 1 (10 Points): Implementation of Command Pattern and REPL
---------------------------------------------------------------------
File: app/commands/__init__.py • Lines ~1-20:
  • Lines ~1-10: Defines the abstract Command base class using the ABC module.
  • Lines ~11-20: Implements the CommandHandler class that registers and executes commands.
File: app/__init__.py • Lines ~1-20:
  • Lines ~1-5: Imports CommandHandler and command plugins.
  • Lines ~6-20: The App class is defined, which initializes CommandHandler, registers commands,
                 and implements the REPL loop (Read, Evaluate, Print, Loop) to process user input.

Requirement 2 (20 Points): Interactive Calculator Commands (add, subtract, multiply, divide)
---------------------------------------------------------------------------------------------
File: app/commands/add/add_command.py • Lines ~1-15:
  • Lines ~1-2: Imports the Command base class and Calculator class.
  • Lines ~3-15: Implements AddCommand with an execute() method that parses two numeric arguments,
                 calls Calculator.add(), and prints the formatted result.
File: app/commands/subtract/subtract_command.py • Lines ~1-15:
  • Implements SubtractCommand similarly, using Calculator.subtract().
File: app/commands/multiply/multiply_command.py • Lines ~1-15:
  • Implements MultiplyCommand similarly, using Calculator.multiply().
File: app/commands/divide/divide_command.py • Lines ~1-20:
  • Implements DivideCommand with proper error handling for division by zero, using Calculator.divide().

Requirement 3 (20 Points): Successful Plugin Architecture Integration for Dynamic Command Loading
-----------------------------------------------------------------------------------------------
File: app/__init__.py • Lines ~21-40:
  • Lines ~21-30: Registers command plugins (add, subtract, multiply, divide, menu, exit)
                 with the CommandHandler.
File: Entire app/commands/ folder structure:
  • Each subfolder (add, subtract, multiply, divide, menu, exit) contains an __init__.py file
    and a corresponding command implementation file, demonstrating a modular plugin architecture.

============================================================
Testing Instructions
============================================================
1. Run all tests:
   Command: pytest
            pytest main.py

2. Check test coverage:
   Command: coverage run -m pytest --num_records=100
            coverage report -m

3. Run the interactive application:
   Command: python main.py
   - At the prompt, test commands such as:
       add 5 3         -> Should output: "The result of 5 add 3 is equal to 8"
       subtract 10 2   -> Should output: "The result of 10 subtract 2 is equal to 8"
       multiply 4 5    -> Should output: "The result of 4 multiply 5 is equal to 20"
       divide 20 4     -> Should output: "The result of 20 divide 4 is equal to 5"
       menu            -> Displays the available commands
       exit            -> Exits the application
============================================================
