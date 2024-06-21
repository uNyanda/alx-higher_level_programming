#!/usr/bin/python3
"""
This module defines a class MyInt that inherits from int and inverts
the behavior of the equality and inequality operators.

Classes:
    MyInt: This class inherits from int and inverts the behavior of
    the equality and inequality operators.
"""


class MyInt(int):
    """
    A class that inherits from int and inverts the behavior of the
    equality and inequality operators.

    Methods:
        __eq__(self, other): Overrides the equality operator.
        __ne__(self, other): Overrides the inequality operator.
    """
    def __eq__(self, other):
        """
        Overrides the equality operator.

        Parameters:
            other (int): The integer to compare with.

        Returns:
            bool: True if self and other are not equal, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the inequality operator.

        Parameters:
            other (int): The integer to compare with.

        Returns:
            bool: True if self and other are equal, False otherwise.
        """
        return super().__eq__(other)
