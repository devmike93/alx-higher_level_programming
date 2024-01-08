#!/usr/bin/python3
"""
This module defines a function to print a formatted message with first and
last names.
"""


def say_my_name(first_name, last_name=""):
    """
    Print a formatted message with the provided first and last names.

    Args:
        first_name (str): The first name to be included in the message.
        last_name (str, optional): The last name to be included in the message.
            Defaults to an empty string.

    Raises:
        TypeError: If either `first_name` or `last_name` is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
