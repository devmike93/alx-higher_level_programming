#!/usr/bin/python3
"""Define a text file-reading function"""


def read_file(filename=""):
    """Read and print the content of a text file (UTF-8 encoded)."""
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
