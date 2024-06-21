#!/usr/bin/python3
"""
This module contains a class 'BaseGeometry' that has 2 public instance
methods 'area' and 'integer_validator'.
"""


class BaseGeometry():
    """
    A class BaseGeometry with 2 public instance methods.

    Methods
    -------
    area(self)
        Raises an Exception.
    integer_validator(self, name, value)
        validates that 'value' is an integer greater than 0.
    """

    def area(self):
        """
        Raises an Exception.

        This method is not implemented and always raises an Exception
        when called.

        Raises:
            Exception: Always, with a message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that 'value' is an integer greater than 0.

        Args:
            name (str): The name of the value.
            value (int): The value to validate.

        Raises:
            TypeError: If 'value' is not an integer.
            ValueError: If 'value' is less than or equal to 0.
        """
        if not isinstance(value, int) or type(value) is bool:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
