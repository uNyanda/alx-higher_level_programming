#!/usr/bin/python3
"""
This module defines a Square class.
"""


class Square:
    """
    This class defines a square by its size,
    with a method to calculate its area.
    """

    def __init__(self, size=0):
        """
        Initialize the Square with optional size.

        Args:
            size (int, optional): Size of the square. Default to 0.
        """
        self.size = size

    @property
    def size(self):
        """int: Property to get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Property setter to set the size of the square.

        Args:
            value (int): Size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculate and return the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square with the character #.

        If size is equal to 0, print an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
