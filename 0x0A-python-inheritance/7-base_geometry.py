#!/usr/bin/python3
"""
Module for BaseGeometry class
"""


class BaseGeometry:
    """
        An empty class representing the base geometry.
    """
    def area(self):
        """
           Raises an Exception with the message "area() is not implemented."
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value as an integer and performs additional checks.

        Args:
            name (str): Name of the value.
            value: Value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
