#!/usr/bin/python3

"""
This module provides a function to divide all
elements of a matrix by a number.

The matrix must be a list of lists of integers
or floats, and each row of the matrix must be of
the same size.
The number to divide by must be an integer or float,
and it cannot be 0.
All elements of the matrix are divided by the number,
and the result is rounded to 2 decimal places.
The function returns a new matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number.

    Args:
        matrix (list): A list of lists of integers or
        floats.
        div (int or float): The number to divide each
        element of the matrix by.

    Returns:
        list: A new matrix with all elements divided
        by div, rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of
        integers/floats, if each row of the matrix does
        not have the same size, or if div is not a number.
        ZeroDivisionError: If div is 0.
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    if not all(isinstance(item, (int, float)) for row in matrix
               for item in row):
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(item / div, 2) for item in row] for row in matrix]
