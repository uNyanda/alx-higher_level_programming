#!/usr/bin/python3
"""
This module returns True if the object is exactly an instance of the specified
class; otherwise False.
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of the specified class.

    Args:
        obj (_type_): The object to check
        a_class (_type_): The class to check against

    Returns:
        bool: True if the object is exactly an instance of the specified class,
        otherwise False.
    """
    return type(obj) is a_class
