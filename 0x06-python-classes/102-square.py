#!/usr/bin/python3
"""
Python file to define a Square
"""


class Square:
    """Square class with private instance attribute size"""

    def __init__(self, size=0):
        """Initializes Square instance with the attribute for size"""
        self.size = size

    @property
    def size(self):
        """Getter method to retrieve the value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set value of size with type and value validation"""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Computes the area of the square"""
        return self.__size ** 2

    def __eq__(self, other):
        """Equality comparison based on area"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Inequality comparison based on area"""
        return self.area() != other.area()

    def __lt__(self, other):
        """Less than comparison based on area"""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal comparison based on area"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Greater than comparison based on area"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal comparison based on area"""
        return self.area() >= other.area()
