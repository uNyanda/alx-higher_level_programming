#!/usr/bin/python3
"""
This module contains a class 'Base'
"""


class Base:
    """
    Base class.

    Attribute:
        __nb_objects:
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes the 'Base' class.

        Args:
            id (int):
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
