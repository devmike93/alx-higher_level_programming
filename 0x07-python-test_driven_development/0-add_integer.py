#!/usr/bin/python3

"""
add_integer Module

This module defines a function to perform integer addition with type checking.
It ensures that both `a` and `b` are integers or floating-point numbers before
performing addition.
"""


def add_integer(a, b=98):
    """
    Perform Integer Addition with Type Checking.

    Parameters:
        a (int or float): The first number.
        b (int or float, optional): The second number (default is 98).

    Returns:
        int: The sum of `a` and `b` as an integer.

    Raises:
        TypeError: If either `a` or `b` is not an integer or float number.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
