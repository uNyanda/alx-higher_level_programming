#!/usr/bin/python3
"""
This module contains a class 'Student' that defines a student by
first_name, last_name, and age.
"""


class Student:
    """
    Defines a Student.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student.

        Args:
            first_name (str): The student's name.
            last_name (str): The student's surname.
            age (str): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        If attrs is a list of strings, only attribute names contained
        in this list must be retrieved. Otherwise, all attributes must
        be retrieved.
        """
        attribute_dict = {}
        if attrs is None:
            return self.__dict__
        elif isinstance(attrs, list):
            for attr in attrs:
                if isinstance(attr, str) and hasattr(self, attr):
                    get_value = getattr(self, attr)
                    attribute_dict[attr] = get_value
            return attribute_dict

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.
        You can assume json will always be a dictionary.
        A dictionary key will be the public attribute name.
        A dictionary value will be the value of the public attribute.
        """
        for key, value in json.items():
            setattr(self, key, value)
