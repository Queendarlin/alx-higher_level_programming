#!/usr/bin/python3
"""Module for Square class that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """The class that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor for Square class."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns the string representation of the Square."""
        return "{} ({}) {}/{} - {}".\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        """Updates the attributes of the Rectangle using *args"""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """Updates the attributes of the Rectangle using *args and kwargs"""
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """Returns the dictionary representation of the Square."""
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
