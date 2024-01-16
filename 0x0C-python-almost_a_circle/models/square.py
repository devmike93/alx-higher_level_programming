#!/usr/bin/python3
"""This module define a square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square instance.

        Args:
            size (int): Size of the square.
            x (int): X-coordinate of the square's position (default 0).
            y (int): Y-coordinate of the square's position (default 0).
            id (int): Unique identifier for the square (default None).
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for the size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size attribute."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the attributes of the Square instance using both positional and
        keyword arguments.

        Args:
            *args: Variable-lenght args in the order: id, size, x and y

        Keyword Args:
            id (int): Update the id attributes.
            size (int): Update the size attribute.
            x (int): Update the x attribute.
            y (int): Update the y attribute.
        """
        if args:
            attributes = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a square instance"""
        return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
                }

    def __str__(self):
        """Returns a string representation of the square"""
        return (
                f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y} - "
                f"{self.width}"
                )
