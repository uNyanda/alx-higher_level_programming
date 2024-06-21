#!/usr/bin/python3

"""
This module provides a function to add two numbers.

The function add_integer(a, b=98) takes two arguments,
a and b. Both a and b should be integers or floats.
If they are not not, function raises a TypeError.
If they are floats, function first casts them to integers.
Function then returns the sum of a and b.
"""


def add_integer(a, b=98):
    """
    Function adds two numbers after
    ensuring they are integers or floats.

    Args:
        a (int, float): The first number to add.
        b (int, float): The second number to add.

    Returns:
        int: The sum of a and b, after casting them
        to integers if they were floats.

    Raises:
        TypeError: If a or b is not integer of float.
    """
    if not isinstance(a, (int, float)) or a != a:
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or b != b:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
