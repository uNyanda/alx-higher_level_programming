#!/usr/bin/python3
"""
This module defines a Square class.
"""


class Square:
    """
    Class defines a square
    with methods to calculate its size
    and position
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
        """
        Property to get the size of square.
        """
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

    @property
    def position(self):
        """
        Property to get the position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Property setter to set the position of the square.

        Args:
            value (tuple): Position of the square as a tuple of
            2 positive integers.

        Raises:
            TypeError: If position is not a tuple of 2 positive
            integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 \
                or not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Calculates and returns the current square area.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square with the character #.

        If size is equal to 0, print an empty line.
        Positioin should be used by using space.
        Don't fill lines by spaces wehn position[i] > 0.
        """
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            print("\n".join(" " * self.__position[0] + "#"
                            * self.__size for _ in range(self.__size)))
