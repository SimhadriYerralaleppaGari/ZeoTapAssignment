# Zeotap Rule Engine with AST

## Project Overview

This project implements a rule engine that determines user eligibility based on attributes like age, department, income, etc. The rules are represented as an Abstract Syntax Tree (AST) to allow dynamic rule creation and evaluation.

## Project Structure

- `src/`: Contains all the source code.
- `tests/`: Contains unit tests.
- `requirements.txt`: Lists project dependencies.

## How to Run

1. Clone the repository.
2. Install the dependencies:
    ```
    pip install -r requirements.txt
    ```
3. Run the main program:
    ```
    python src/main.py
    ```
4. To run the tests:
    ```
    python -m unittest discover -s tests
    ```

## Files

- `ast_node.py`: Contains the AST Node class.
- `rule_parser.py`: Logic to parse rule strings into an AST.
- `rule_combiner.py`: Combines multiple ASTs into one.
- `rule_evaluator.py`: Evaluates rules against user data.
- `database.py`: Optional database handling for rule storage.
