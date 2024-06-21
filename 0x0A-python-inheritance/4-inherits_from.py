#!/usr/bin/python3
"""
This module contains a function that checks if the object is an instance of a
class that inherited (directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False

    Args:
        obj (_type_): The object to check.
        a_class (_type_): The class to check against.

    Returns:
        bool: True if the object is an instance of a class that inherited from
        the specified class, otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
