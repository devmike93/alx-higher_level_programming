#!/usr/bin/python3
"""This module defines a function for matrix multiplication"""


def matrix_mul(m_a, m_b):
    """
    Multiply two matrices.
    The function takes two matrices represented as lists of lists and returns
    their product as a list of lists. It also performs input validation and
    raises appropriate errors for invalid input or incompatible matrices.

    Args:
        m_a (list of lists): The first matrix represented as a list of lists.
        m_b (list of lists): The second matrix represented as a list of lists.

    Returns:
        list of lists: The result of matrix multiplication as a list of lists.

    Raises:
        Raise a TypeError:
        - If either m_a or m_b is not a list or if they are not lists of lists
        - If any element in m_a or m_b is not an integer or a float.
        - If the rows in m_a or m_b are not of the same size.
        - If m_a and m_b cannot be multiplied due to incompatible dimensions.
        Raise a ValueError:
        - If either m_a or m_b is empty or contains empty rows.
    """

    # Check if m_a or m_b is not a list
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # Check if m_a or m_b is not a list of lists
    if all(not isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if all(not isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # Check if m_a or m_b is empty
    if not m_a or len(m_a) is 0 or all(not row for row in m_a):
        raise ValueError("m_a can't be empty")
    if not m_b or len(m_b) is 0 or all(not row for row in m_b):
        raise ValueError("m_b can't be empty")

    # check if one element of those list of lists is not an integer or a float
    if any(not isinstance(i, (int, float)) for row in m_a for i in row):
        raise TypeError("m_a should contain only integers or floats")
    if any(not isinstance(i, (int, float)) for row in m_b for i in row):
        raise TypeError("m_b should contain only integers or floats")

    # if m_a or m_b is not a rectangle (all ‘rows’ should be of the same size)
    if any(len(row) != len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # check if m_a and m_b can’t be multiplied
    if len(m_a[0]) != len(m_b):
        raise TypeError("m_a and m_b can't be multiplied")

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]

    # Perform matrix multiplication
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]
    return (result)
