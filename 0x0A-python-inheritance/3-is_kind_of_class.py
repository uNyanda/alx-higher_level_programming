#!/usr/bin/python3
"""
This module returns True if the object is an instance of, or if the object
is an instance of a class that inherited from, the specified class; otherwise
False.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of the specified class or a subclass
    thereof.

    Args:
        obj (_type_): The object to check.
        a_class (_type_): The class to check against

    Return:
        bool: True if the object is an instance of the specified class or
        a subclass thereof, otherwise False.
    """
    return isinstance(obj, a_class)
