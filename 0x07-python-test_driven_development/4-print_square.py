#!/usr/bin/python3
"""
Print_square Module:
    Prints out a square to the terminal, made up of #
"""


def print_square(size):
    """
    Print a square of '#' characters.

    This function takes an integer 'size' as input and prints a square pattern
    of '#' characters with the given size. If 'size' is less than 0 or not an
    integer, it raises appropriate exceptions.

    Args:
        size (int): The size of the square to be printed.

    Raises:
        TypeError: If 'size' is not an integer.
        ValueError: If 'size' is less than 0.
    """
    if not isinstance(size, (int)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        [print("#", end='') for j in range(size)]
        print()
