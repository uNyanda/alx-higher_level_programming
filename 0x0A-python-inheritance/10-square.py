#!/usr/bin/python3
"""
This module defines a class 'Square' that inherits from the
'Rectangle' class.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a Square.

    This class inherits from the 'Rectangle' class and
    is initialized with 'size' which is validated by the
    integer_validator method from BaseGeometry class inherited
    by Rectangle class.

    Args:
        __size (int): Size of the square.
    """

    def __init__(self, size):
        """
        Initializes the 'Square'.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is not greater than 0.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Returns the area of the square.
        """
        return self.__size ** 2
