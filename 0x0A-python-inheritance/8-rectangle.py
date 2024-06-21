#!/usr/bin/python3
"""
This module defines a class 'Rectangle' that inherits a 'BaseGeometry' class.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a Rectangle with width and height.

    The Rectangle class inherits from the BaseGeometry class and
    initializes with a width and height that are validated by the
    integer_validator method in the BaseGeometry class.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.

    Methods
    -------
        __init__(self, width, height): Initializes a Rectangle instance.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            Both must be positive integers.

        Raises:
            TypeError: If width or height are not integers.
            ValueError: If width or height are not greater than 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
