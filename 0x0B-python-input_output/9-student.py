#!/usr/bin/python3
"""
This module contains a class 'Student' that defines a student.
"""


class Student():
    """
    Defines a Student by their first_name, last_name and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes the Student.

        Args:
            first_name (str): The name of the student.
            last_name (str): The student's surname.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.

        Returns:
            A dictionary representation of the Student.
        """
        return self.__dict__
