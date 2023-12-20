#!/usr/bin/python3
"""
Python file for a MagicClass class
"""


import math


class MagicClass:
    """Python class MagicClass equivalent to given bytecode."""

    def __init__(self, radius=0):
        """Initialize MagicClass instance with radius."""
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self._MagicClass_radius = radius

    def area(self):
        """Calculate and return the area."""
        return self._MagicClass_radius ** 2 * math.pi

    def circumference(self):
        """Calculate and return the circumference."""
        return 2 * math.pi * self._MagicClass_radius
