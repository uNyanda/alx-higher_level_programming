#!/usr/bin/python3
"""
This module defines a Square class.
"""


class Square:
    """This is a Square class."""

    def __init__(self, size=0):
        """
        Initialize the Square.

        Parameters:
            size (int): The size of the Square. Default is 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        This module returns the current square area.
        """
        return self.__size ** 2
