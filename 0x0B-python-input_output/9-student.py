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

    def to_json(self):
        """
                Retrieves a dictionary representation of a Student instance.

                Returns:
                    dict: Dictionary representation of the Student instance.
                """
        return self.__dict__
