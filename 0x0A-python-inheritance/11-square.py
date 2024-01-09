#!/usr/bin/python3
"""Module to define class Square"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Class Square; inherits from Rectangle"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Return a string representation of the Square class"""
        return f"[Square] {self.__size}/{self.__size}"
