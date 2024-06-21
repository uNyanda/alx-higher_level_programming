#!/usr/bin/python3
"""
This module contains a class 'BaseGeometry' that has public instance method
'area' that raises an Exception.
"""


class BaseGeometry():
    """
    A class BaseGeometry with a public instance method.

    Methods
    -------
    area(self)
        Raises an Exception with the message 'area() is not implemented'.
    """

    def area(self):
        """
        Raises an Exception.
        This method is not implemented and always raises an Exception when
        called.

        Raises:
            Exception: Always, with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")
