#!/usr/bin/python3
"""
This module contains a function that returns an object (Python data structure)
represented by a JSON string.
"""
import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON
    string.

    Args:
        my_str: the string to return.

    Returns:
        my_str (a json string).
    """
    return json.loads(my_str)
