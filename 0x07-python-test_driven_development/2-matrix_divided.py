#!/usr/bin/python3
"""Defines a matrix division function."""


def matrix_divided(matrix, div):
    """
    Divide each element of a matrix by a specified divisor.

    Args:
        matrix (list of lists): The matrix to be divided.
        div (int or float): The divisor to divide each elmnt of the matrix by.

    Returns:
        list of lists: A new matrix representing the result of the division.

    Raises:
        TypeError:
        - If the input matrix is not a list of lists
        - If it contains non-integer or non-float elements
        - If has rows of different sizes
        - Also raised if 'div' is not a number (int or float).
        ZeroDivisionError: If 'div' is equal to zero.

    Note:
        - The result is rounded to two decimal places.
        - The input matrix is not modified; a new matrix is returned.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    message = "matrix must be a matrix (list of lists) of integers/floats"
    if matrix is None or len(matrix) == 0 or not isinstance(matrix[0], list):
        raise TypeError(message)
    new_matrix = []
    lenght = len(matrix[0])
    for row in matrix:
        if len(row) != lenght:
            raise TypeError("Each row of the matrix must have the same size")
        if (not row or
                not isinstance(row, list) or
                not (all(isinstance(digit, (int, float)) for digit in row))):
            raise TypeError(message)

        new_row = [round(digit / div, 2) for digit in row]
        new_matrix.append(new_row)

    return (new_matrix)
