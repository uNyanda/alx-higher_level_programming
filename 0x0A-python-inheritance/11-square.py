#!/usr/bin/python3
"""
This module defines a class 'Square' that inherits from the 'Rectangle'
class.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a Square.

    This class inherits from the Rectangle class and initializes
    with a size that is validated by the integer_validator method
    from the BaseGeometry class.

    Args:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes the Square.

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
        Returns the Square area.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns the string representation of Square.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
