"""
simple_calculator.py
This module provides basic arithmetic operations: addition, subtraction,
multiplication, and division. It can be used for simple mathematical calculations.
"""
def add(a, b):
    """
    Add two numbers.

    Parameters
    ----------
    a : int or float
        First number.
    b : int or float
        Second number.
    Returns
    -------
    int or float
        Sum of a and b.
    """
    return a + b
def subtract(a, b):
    """
    Subtract b from a.

    Parameters
    ----------
    a : int or float
        First number.
    b : int or float
        Second number.
    Returns
    -------
    int or float
        Result of a - b.
    """
    return a - b
def multiply(a, b):
    """
    Multiply two numbers.

    Parameters
    ----------
    a : int or float
        First number.
    b : int or float
        Second number.
    Returns
    -------
    int or float
        Product of a and b.
    """
    return a * b
def divide(a, b):
    """
    Divide a by b.
    Parameters
    ----------
    a : int or float
        Numerator.
    b : int or float
        Denominator.
    Returns
    -------
    float
        Result of a / b.

    Raises
    ------
    ZeroDivisionError
        If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b
# Test the functions
if __name__ == "__main__":
    a = 10
    b = 5
    print("Addition:       ", add(a, b))
    print("Subtraction:    ", subtract(a, b))
    print("Multiplication: ", multiply(a, b))
    print("Division:       ", divide(a, b))
