#!/usr/bin/python3
"""
This module defines a 'Rectangle' class that imports from a 'BaseGeometry'
class.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle.

    This class inherits from the BaseGeometry class and
    initializes with a width and height that are validated by the
    integer_validator method in the BaseGeometry class.

    Attributes:
        __width (int): The width of the rectangle. Must be a positive integer
        __height (int): The height of the rectangle. Must be a positive integer
    """

    def __init__(self, width, height):
        """
        Initializes the Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If height or width are not integers.
            ValueError: If height or width are not greater than 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Returns the area of the Rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns the string representation of Rectangle.

        Returns:
            A formatted string "[Rectangle] <width>/<height>".
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
