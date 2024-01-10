#!/usr/bin/python3
"""Define a Pascals triangle function"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle as a list of lists of integers for a given
    value of n.

    Args:
        n (int): The number of rows in Pascal's triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = []
    for row in range(n):
        cur_row = [1]
        if row > 0:
            prev_row = triangle[row - 1]
            for i in range(1, row):
                cur_mid_val = prev_row[i - 1] + prev_row[i]
                cur_row.append(cur_mid_val)
            cur_row.append(1)
        triangle.append(cur_row)
    return triangle
