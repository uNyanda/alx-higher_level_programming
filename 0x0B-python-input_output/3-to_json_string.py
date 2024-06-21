#!/usr/bin/python3
"""
This module contains a function that returns the JSON representation
of an object (string).
"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj: the object to return JSON representation of.

    Returns:
        the JSON representation of my_obj.
    """
    return json.dumps(my_obj)
