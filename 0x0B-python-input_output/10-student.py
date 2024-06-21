#!/usr/bin/python3
"""
This module contains a class 'Student' that defines a student by
first_name, last_name, and age.
"""


class Student:
    """
    Defines a Student by first_name, last_name and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student.

        Args:
            first_name (str): The student's name.
            last_name (str): The student's surname.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        """
        # initialize an empty dictionary to store the attributes.
        attribute_dict = {}
        if isinstance(attrs, list):
            for attr in attrs:
                # check if attribute is a string and exits in Student instance
                if isinstance(attr, str) and hasattr(self, attr):
                    # get the value of the attribute.
                    attr_value = getattr(self, attr, None)
                    # add the attribute and its value to the dictionary.
                    attribute_dict[attr] = attr_value
        else:
            # if attrs is not a list, retrieve all attributes.
            attribute_dict = self.__dict__
        # return the dictionary of attributes.
        return attribute_dict
