#!/usr/bin/python3
"""
This module contains a function 'class_to_json' that returns the dictionary
description with simple data structure (list, dictionary, string, integer and
boolean) for JSON serialization of an object.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization of
    an object.

    Args:
        obj: an instance of a Class.

    Returns:
        the dictionary description of obj.
    """
    # get the dictionary representation of obj
    obj_dict = obj.__dict__

    # initialize an empty dictionary to store the attributes with simple
    # data structures.
    simple_data_structure_dict = {}

    # iterate over each attribute in obj_dict
    for key, value in obj_dict.items():
        # check if the attribute's data type is list, dict, str, int, or bool
        if type(value) in [list, dict, str, int, bool]:
            # if it is, add it to simple_data_structure_dic
            simple_data_structure_dict[key] = value
    # return the dictionary of attributes with simple data structures
    return simple_data_structure_dict
