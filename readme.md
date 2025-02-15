Calculator Assignment Requirements Mapping
============================================

Requirement 1 (30 Points): Faker Integration
---------------------------------------------------------
File: requirements.txt
  • Faker is installed via "pip install faker" and appears in requirements.txt
    after running "pip freeze > requirements.txt".

File: tests/test_faker.py • Lines ~1-9:
  • Lines 1-2: Import Faker and the Calculator class.
  • Lines 3-9: A test (test_faker_addition) creates a Faker() instance, generates random integers,
    computes the expected sum, and asserts that Calculator.add returns the correct result.

Requirement 2 (30 Points): Test Data Generation using Pytest Command-Line Option
---------------------------------------------------------
File: tests/conftest.py • Lines ~1-37:
  • Lines 1-8: Defines pytest_addoption to add the "--num_records" command-line option.
  • Lines 10-37: Implements the fake_records fixture that uses Faker to generate a list of test records
    (tuples with two numbers, an operator, and the expected result) based on the --num_records value.

File: tests/test_generated_data.py • Lines ~1-16:
  • Lines 1-4: Defines a test (test_generated_records_structure) that uses the fake_records fixture.
  • Lines 5-16: Verifies that each generated record is a tuple of 4 elements, and that each element meets
    the expected type and value constraints.

(Optional)
File: tests/test_conftest_extras.py • Lines ~1-20:
  • Additional tests simulate scenarios (e.g., num_records=0 and forcing an exception branch)
    to ensure all branches in the fake_records fixture are executed, helping achieve 100% coverage.

Requirement 3 (40 Points): User Input Handling via Command-Line Application
---------------------------------------------------------
File: main.py • Lines ~1-40:
  • Lines 1-3: Imports necessary modules and Calculator classes.
  • Lines ~5-14: The parse_args function converts command-line arguments (a, b, and operation) into proper types,
    raising an error for invalid input.
  • Lines ~16-29: The perform_operation function maps the operation string to the corresponding Calculator method,
    handling errors such as divide-by-zero and unknown operations.
  • Lines ~31-38: The main() function calls parse_args and perform_operation, printing the result or an error message.

========================
Testing Instructions
========================

1. Run all tests (with fake records generated):
   - Command: 
     pytest --num_records=100
     
2. Run tests with output (disable capturing):
   - Command:
     pytest --num_records=100 -s
     
3. Check test coverage:
   - Command:
     coverage run -m pytest --num_records=100
     coverage report -m
     
4. Test the command-line application (User Input Handling):
   - Example Commands:
     python main.py 5 3 add
     python main.py 1 0 divide
     python main.py 9 3 unknown
     python main.py a 3 add
     python main.py 5 b subtract

============================================================
