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

    def __eq__(self, other):
        """
        Check if the are of the square is equal to the area
        of another square.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the areas are equal. False otherwise.
        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """
        Check if the area of this square is not equal to the area
        of another square.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the areas are not equal, False otherwise.
        """
        return not self.__eq__(other)

    def __lt__(self, other):
        """
        Checks if the area of this square is less than the area of
        another square.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if this square's area is less, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return False

    def __le__(self, other):
        """
        Checks if the area of this square is less than or equal to
        the area of another square.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if this square's area is less than or equal
            to the other's, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() <= other.area()
        return False
