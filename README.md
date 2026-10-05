# PLP Python Week 6 - Safe Functions

This assignment practices error handling using `try` and `except` in Python.

## Files

* `safe_tools.py` - Contains three safe functions for division, converting text to numbers, and looking up dictionary fields.
* `unbreakable.py` - Demonstrates how `try` and `except` can keep a program running when invalid input is entered.
* `README.md` - Provides information about the assignment and the files.

## Why can the `if` check not catch `abc` on its own?

An `if` check can test whether a value meets a condition, but converting `"abc"` using `int()` causes a `ValueError` before the program can continue. Using `try` and `except ValueError` allows the program to catch the error and handle it safely instead of crashing.

## Expected Output

```text
5.0
Cannot divide by zero
42
Not a number
82
Field not found

