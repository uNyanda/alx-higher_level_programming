#!/usr/bin/python3
"""
This module defines a function add_attribute that adds a new attribute
to an object if it's possible.

Functions:
    add_attribute(obj, attr, value): Adds a new attribute to an object
    if it's possible.
"""


def add_attribute(obj, attr, value):
    """
    Adds a new attribute to an object if it's possible.

    Parameters:
        obj (object): The object to add the attribute to.
        attr (str): The name of the attribute.
        value: The value of the attribute.

    Raises:
        TypeError: If the object can't have new attributes added.
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
