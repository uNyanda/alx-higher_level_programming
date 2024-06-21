#!/usr/bin/python3
"""
This module contains a function that returns a list of lists of integers
representinf the Pascal's triangle of n.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    the Pascal's triangle of n.

    Args:
        n (int): the number of rows to print the triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for row_number in range(1, n):
        current_row = [1]
        previous_row = triangle[-1]

        for index in range(len(previous_row) - 1):
            sum_of_two_elements = previous_row[index] + previous_row[index + 1]
            current_row.append(sum_of_two_elements)
        current_row.append(1)
        triangle.append(current_row)
    return triangle
