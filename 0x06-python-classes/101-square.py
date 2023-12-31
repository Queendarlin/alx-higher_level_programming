#!/usr/bin/python3
"""
Python file to define a Square
"""


class Square:
    """Square class with private instance attribute size"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes Square instance with the attribute for size"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter method to retrieve the value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set value of size with type and value validation"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter method to retrieve the value of position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method for type and value validation"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(index, int) for index in value) or
                any(index < 0 for index in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Computes the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for index in range(self.__position[1]):
                print()
            for index in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Returns a string representation of the square"""
        if self.__size != 0:
            [print("") for itr1 in range(0, self.__position[1])]
        for itr1 in range(0, self.__size):
            [print(" ", end="") for itr2 in range(0, self.__position[0])]
            [print("#", end="") for itr3 in range(0, self.__size)]
            if itr1 != self.__size - 1:
                print("")
        return ("")
