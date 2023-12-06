#!/usr/bin/python3
"""
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_row = list(map(lambda x: x**2, row))
        new_matrix.append(new_row)
    return new_matrix
"""


def square_matrix_simple(matrix=[]):
    # Create a new matrix using list comprehension with element-wise squaring
    new_matrix = [[x**2 for x in row] for row in matrix]
    return new_matrix
