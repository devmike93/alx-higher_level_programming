#!/usr/bin/python3
"""Module to define class BaseGeometry"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle; inherits from BaseGeometry"""

    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return a string representation of the rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"
