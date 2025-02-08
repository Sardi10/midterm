Calculator Assignment Requirements Mapping
============================================

Requirement 1 (20 Points): Arithmetic Operations (Add, Subtract, Multiply, Divide)
-------------------------------------------------------------------------
- File: calculator/calculator.py
  • Lines ~3-17: 
    - The static methods add, subtract, multiply, and divide are implemented.
    - Each method creates a Calculation instance and calls its perform() method.

Requirement 2 (10 Points): Exception Throwing and Testing for Divide-by-Zero
-------------------------------------------------------------------------
- File: calculator/calculation.py
  • Lines ~15-19:
    - In the perform() method, when the operator is '/' and operand2 is zero,
      a ZeroDivisionError is raised.
- File: tests/test_calculator.py
  • Lines ~35-39:
    - The test_divide_by_zero function uses pytest.raises(ZeroDivisionError)
      to verify that dividing by zero raises an exception.

Requirement 3 (30 Points Each): Use of Static, Class, and Instance Methods
-------------------------------------------------------------------------
- Static Methods:
  • File: calculator/calculator.py
    - Lines ~3-17: The add, subtract, multiply, and divide methods are declared as static.
- Instance Methods:
  • File: calculator/calculation.py
    - Lines ~3-10: The __init__ method and perform() method are instance methods for the Calculation class.
  • File: calculator/calculations.py
    - Lines ~3-7: The __init__ method initializes the history list (instance-level data).
- Class Method:
  • File: calculator/calculations.py
    - Lines ~21-29: The from_operations method is implemented as a class method to create a Calculations instance from a list of operations.

Requirement 4 (5 Points): Calculation Class Storing the Arithmetic Operation
-------------------------------------------------------------------------
- File: calculator/calculation.py
  • Lines ~3-10:
    - The __init__ method stores operand1, operand2, and operator as instance properties,
      along with initializing the result property.

Requirement 5 (15 Points): Calculation History to Store Calculation Instances
-------------------------------------------------------------------------
- File: calculator/calculations.py
  • Lines ~3-7:
    - The __init__ method initializes a history list (self.history) to store Calculation objects.

Requirement 6 (10 Points): Convenience Methods on the Calculations Class to Manage History
-------------------------------------------------------------------------
- File: calculator/calculations.py
  • Lines ~9-19:
    - Methods add_calculation (adds a Calculation instance),
      get_last (retrieves the most recent calculation), and clear_history (clears the history)
      provide convenient history management.

Requirement 7 (10 Points): Using Parameterized Test Data
-------------------------------------------------------------------------
- File: tests/test_calculator.py
  • Lines ~3-7 (and similar blocks for each operation):
    - The @pytest.mark.parametrize decorators are used to supply multiple data sets for tests
      on add, subtract, multiply, and divide operations.
