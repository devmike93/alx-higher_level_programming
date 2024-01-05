#!/usr/bin/python3
"""
This module represents a Class rectangle
"""


class Rectangle:
    """ This class represents an empty rectangle. """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """Return a string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return ('\n'.join(['#' * self.__width for _ in range(self.__height)]))
        """
        underscore expanation in loop:
        The _ within the list comprehension indicates that the loop variable
        from range(self.__height) is not being used.
        The underscore serves as a placeholder to signify
        that the loop is iterating over the range,
        but the loop variable itself is not used within the list comprehension.

        if self.__width == 0 or self.__height == 0:
        return ""  # Returns an empty string if either width or height is zero

        rectangle_str = ""
        for _ in range(self.__height):
            # Create a row of '#' characters based on width
            row = '#' * self.__width
            rectangle_str += row + '\n'  # Append the row followed by a newline
        # Remove the trailing newline and return the rectangle string
        return rectangle_str.rstrip('\n')
        """
