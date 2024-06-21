#!/usr/bin/python3
"""
This module contains a function that creates an Object from a "JSON file".
"""
import json


def load_from_json_file(filename):
    """
    Creates an Object from a "JSON file".

    Args:
        filename: the name of the file to create an Object from.

    Returns:
        the object created from the json file.
    """
    with open(filename, mode="r") as file:
        return json.load(file)
