#!/usr/bin/python3
"""Define a function that appends a string at the end of a file"""


def append_write(filename="", text=""):
    """
    Append a string to the end of a text file (UTF-8 encoded).

    Args:
    filename (str): The name of the text file to append to.
    text (str): The string to append to the file.

    Returns:
    int: The number of characters added to the file.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
