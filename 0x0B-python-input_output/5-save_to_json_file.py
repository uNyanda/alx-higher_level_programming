#!/usr/bin/python3
"""
This module contains a function that writes an Object to a text file,
using JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file, using JSON representation.

    Args:
        my_obj: the object to write to a text file.
        filename: the file to write to.
    """
    with open(filename, mode="w") as file:
        json.dump(my_obj, file)
