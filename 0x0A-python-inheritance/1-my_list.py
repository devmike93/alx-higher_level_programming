#!/usr/bin/python3
"""Defines an inherited list class MyList"""


class MyList(list):
    """
    A custom list class that inherits from the built-in list class and provides
    additional functionality for printing the list in ascending sorted order.
    """

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))
