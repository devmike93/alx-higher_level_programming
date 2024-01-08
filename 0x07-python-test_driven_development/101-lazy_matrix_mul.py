#!/usr/bin/python3
"""Defines a matrix multiplication function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Perform matrix multiplication using NumPy.

    Args:
        m_a (list of lists): The first matrix as a list of lists.
        m_b (list of lists): The second matrix as a list of lists.

    Returns:
        list of lists: The result of matrix multiplication as a list of lists.

    """
    return (np.matmul(m_a, m_b))
