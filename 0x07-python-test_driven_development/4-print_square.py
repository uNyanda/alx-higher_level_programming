#!/usr/bin/python3

"""
This module defines a function that prints
a square with the character #
"""


def print_square(size):
    """
    Prints a square with the character #.

    Args:
        size (int): The length of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if isinstance(size, (str, float)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)


def wrapper_square(*args):
    """
    Wrapper function for print_square.

    Args:
        *args: variable length argument list.
    """
    if len(args) == 0:
        print("No argument provided to print_square")
    else:
        try:
            print_square(args[0])
        except Exception as e:
            print(f"1 argument required: {e}")
