# tdd-palindrome-unittest

This repository demonstrates a complete 

**Test-Driven Development (TDD)**
workflow in python. 
It includes a palindrome checker and a CI/CD pipeline using GitHub Actions.

## project structure

- `main.py` contains the `is_palindrome` implementation
- `test_palindrome.py` contains the test suite
- `test_smoke.py` contains a test smoke implementation to configure environment

- This project followed the **Red-Green-Refractor** cycle:
1. **Red** Write a failing test for a new requirement
2. **Green** Implement minimal code to pass the test
3. **Refractor** Optimise and clean the code

Running tests locally:
- Ensure you have python3.11+ installed then run:
```bash -python3 -m unittest discover