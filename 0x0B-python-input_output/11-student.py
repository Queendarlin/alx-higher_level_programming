#!/usr/bin/python3
"""
Module for Student class
"""


class Student:
    """
        Class representing a student.

        Attributes:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
    """
    def __init__(self, first_name, last_name, age):
        """
            Initializes a new instance of the Student class.

            Args:
                first_name (str): The first name of the student.
                last_name (str): The last name of the student.
                age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
                Retrieves a dictionary representation of a Student instance.

            Args:
                attrs (list): List of attribute names to be retrieved.
                Default is None.

            Returns:
                    dict: Dictionary representation of the Student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """
                Replaces all attributes of the Student instance.

                Args:
                    json (dict): Dictionary with attribute names and values
                """
        for key, value in json.items():
            setattr(self, key, value)
