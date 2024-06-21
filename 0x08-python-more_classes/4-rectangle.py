#!/usr/bin/python3

"""
This module defines a Rectangle class for representing rectangles.

This class has 2 private instance attributes:
width and height.
Both attributes must be integers and greater than or equal to 0.
If non-integer or negative integer is provided, a TypeError
or ValueError will be raised respectively.

The Rectangle class provides getter and setter methods for both
attributes.

This class has 2 public instance methods:
area and perimeter, which return the rectangle area and rectangle
perimeter.
If width or height is equal to 0, perimeter is equal to 0.
print() and str() should print the rectangle with the character #
If width or height is equal to 0, an empty string must be returned.

repr() should return a string representation of the rectangle to be
able to recreate a new instance by using eval().
"""


class Rectangle:
    """
    Defines a Rectangle class.
    """
    def __init__(self, width=0, height=0):
        """
        Constructor for the Rectangle class.

        Args:
            width (int): The width of the rectangle.
                        Defaults to 0.
            height (int): The height of the rectangle.
                        Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        The getter for the width attribute.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        The setter for the width attribute.

        Args:
            value (int): The width of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if isinstance(value, (float, str)):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height attribute.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height attribute.

        Args:
            int: The height of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if isinstance(value, (float, str)):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns the rectangle area.
        """
        area = self.width * self.height
        return area

    def perimeter(self):
        """
        Returns the rectangle perimeter.
        """
        if self.width == 0 or self.height == 0:
            return 0
        perimeter = 2 * self.width + 2 * self.height
        return perimeter

    def __str__(self):
        """
        Prints the rectangle with the character #
        """
        result = ""  # empty string
        if self.width == 0 or self.height == 0:
            return result
        for _ in range(self.height):
            result += '#' * self.width + '\n'
        return result.rstrip('\n')  # trailing newline

    def __repr__(self):
        """
        Returns the string representation of the rectangle.
        """
        return "Rectangle({}, {})".format(self.width, self.height)
