#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i, row in enumerate(matrix):
        for j, element in enumerate(row):
            # checks if the current element is not the last element in the row.
            if j < len(row) - 1:
                print("{:d}".format(element), end=' ')
            else:  # if last element in row
                print("{:d}".format(element), end='')
        print()


"""
Using enumerate() simplifies the code by providing the index values
(i for rows and j for elements within rows)
alongside the elements themselves.
This is particularly useful when you need to know both the position
and the value of elements while iterating through sequences in Python.
"""
