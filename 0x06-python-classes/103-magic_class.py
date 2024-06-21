#!/usr/bin/python3
"""This module defines a class MagicClass."""
import math


class MagicClass:
    """
    This class defines a MagicClass by its
    radius with methods to calculate
    its area and its circumference.
    """

    def __init__(self, radius=0):
        """
        Initialize a new instance of MagicClass.

        Args:
            radius (int, float): The radius of the circle. Defaults to 0.

        Raises:
            TypeError: If radius is not a number (int or float).
        """
        if not isinstance(radius, (int, float)):
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculate the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
