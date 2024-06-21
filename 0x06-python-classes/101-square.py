#!/usr/bin/python3

"""This module defines a Square class."""


class Square:
    """
    Defines a square
    with methods to calculate its size
    and position.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize Square instance with size and position.

        Args:
            size (int, optional): Size of square. Default to 0.
            position (tuple, optional): Position of square as a
            tuple of 2 postive integers. Defaults to (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Property to get size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Property to set size of square.

        Args:
            value (int): Size of square

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

    @property
    def position(self):
        """Property to get position of square."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Property to set position of square.

        Args:
            value (tuple): Position of square as a
            tuple of 2 positive integers. Default to 0.

        Raises:
            TypeError: If position is not a tuple of
            2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 \
                or not all(isinstance(num, int) for num in value) \
                or any(num < 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character #"""
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            print((" " * self.__position[0] + "#" * self.__size + "\n")
                  * self.__size, end="")

    def __str__(self):
        """Returns a string representation of the square"""
        if self.__size == 0:
            return ""
        else:
            return ("\n" * self.__position[1] + (" "
                    * self.__position[0] + "#" *
                    self.__size + "\n") * (self.__size - 1) +
                    " " * self.__position[0] + "#" * self.__size)
