#!/usr/bin/python3
"""Defines an empty class BaseGeometry"""


class BaseGeometry:
    """A base class for geometry-related classes."""
    def area(self):
        """
        Raises an Exception indicating that the area() method is not
        implemented.
        """
        raise Exception("area() is not implemented")
