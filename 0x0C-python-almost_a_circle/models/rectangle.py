#!/usr/bin/python3
"""
This module contains a class 'Rectangle' that inherits from 'Base' class.
"""
from models.base import Base


class Rectangle(Base):
    """
    Class 'Rectangle' inherits from 'Base' class.

    This class includes methods for setting and getting the width, height,
    x and y attributes.
    It also include methods for the area of the rectangle, for
    displaying the rectangle, for assigning an argument to each attribute.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes the 'Rectangle' class.

        Args:
            width(int): the width of the rectangle.
            height(int): the height of the rectangle.
            x (int): the horizontal distance of the rectangle.
            y (int): the vertical distance of the rectange.
            id (int, optional): The identifier for the rectangle.
                                Defauls to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter for the 'width' attribute.
        Gets the width of the rectangle.

        Returns:
            int: The 'width' of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the 'width' attribute.
        Sets the width of the rectangle.

        Args:
            value(int): the new value to be set for the 'width'.

        Raises:
            TypeError: If 'width' is not an integer.
            ValueError: If 'width' is under or equals to 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the 'height' attribute.
        Gets the height of the rectangle.

        Returns:
            int: The 'height' of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the 'height' attribute.
        Sets the height of the rectangle.

        Args:
            value (int): the new value to be set for the 'height'.

        Raises:
            TypeError: If 'height' is not an integer.
            ValueError: If 'height' is under or equals to 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Property getter for the 'x' attribute.
        Gets the x coordinate of the rectangle.

        Returns:
            int: The 'x' coordinate.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Property setter for the 'x' attribute.
        Sets the 'x' coordinate of the rectangle.

        Args:
            value (int): The value of the 'x' coordinate.

        Raises:
            TypeError: If 'y' is not an integer.
            ValueError: If 'y' is under 0.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Property getter for the 'y' attribute.
        Gets the 'y' coordinate of the rectangle.

        Returns:
            int: The 'y' coordinate.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Property setter for the 'y' attribute.
        Sets the 'y' coordinate of the rectangle.

        Args:
            value (int): The value of the 'y' coordinate.

        Raises:
            TypeError: If 'y' is not an integer.
            ValueError: If 'y' is under 0.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculates the area value of the 'Rectangle' instance.

        Returns:
            The area of the 'Rectangle'.
        """
        area = self.__width * self.__height
        return area

    def display(self):
        """
        Prints the 'Rectangle' instance with the character '#',
        taking care of 'x' and 'y'.
        """
        print('\n' * self.__y, end='')  # Print vertical
        for _ in range(self.__height):
            print(' ' * self.__x, end='')  # Print horizontal
            print('#' * self.__width)

    def __str__(self):
        """
        Returns a string representation of the Rectangle instance.

        Returns:
            str: A string in the format
                    '[Rectangle] (<id>) <x>/<y> - <width>/<height>'.
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.__x, self.__y,
                        self.__width, self.__height))

    def update(self, *args):
        """
        Assigns an argument to each attribute.

        Args:
            *args: variable length argument.
        """
        attributes = ['id', '_Rectangle__width', '_Rectangle__height',
                      '_Rectangle__x', '_Rectangle__y']
        for attribute, value in zip(attributes, args):
            setattr(self, attribute, value)
