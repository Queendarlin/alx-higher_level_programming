#!/usr/bin/python3
"""
Module for Base class
"""
import json
import csv


class Base:
    """Base class for managing id attribute in other classes."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor for Base class."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts a list of dictionaries to a JSON string."""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""
        if list_objs is None:
            list_objs = []
        else:
            list_objs = [obj.to_dictionary() for obj in list_objs]
        with open("{}.json".format(cls.__name__), "w",
                  encoding="utf-8") as file:
            file.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string."""
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set."""
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            dummy_instance = Rectangle(1, 1)
        elif cls is Square:
            dummy_instance = Square(1)
        else:
            dummy_instance = None
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a JSON file."""
        from os import path
        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, "r", encoding="utf-8") as fr:
            return [cls.create(**s) for s in cls.from_json_string(fr.read())]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes a list of instances to a CSV file."""
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[ob.id, ob.width, ob.height, ob.x, ob.y]
                             for ob in list_objs]
            else:
                list_objs = [[ob.id, ob.size, ob.x, ob.y]
                             for ob in list_objs]
        with open('{}.csv'.format(cls.__name__), 'w', newline='',
                  encoding='utf-8') as fi:
            writer = csv.writer(fi)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes instances from a CSV file."""
        from models.rectangle import Rectangle
        from models.square import Square
        deserialized_instance = []
        with open('{}.csv'.format(cls.__name__), 'r', newline='',
                  encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                row = [int(row_element) for row_element in row]
                if cls is Rectangle:
                    dictionary = {"id": row[0], "width": row[1],
                                  "height": row[2], "x": row[3], "y": row[4]}
                else:
                    dictionary = {"id": row[0], "size": row[1],
                                  "x": row[2], "y": row[3]}
                deserialized_instance.append(cls.create(**dictionary))
        return deserialized_instance

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws Rectangles and Squares using the Turtle graphics module."""
        import turtle
        import time
        from random import randrange
        turtle.Screen().colormode(255)
        for rect in list_rectangles + list_squares:
            t = turtle.Turtle()
            t.color((randrange(255), randrange(255), randrange(255)))
            t.pensize(1)
            t.penup()
            t.pendown()
            t.setpos((rect.x + t.pos()[0], rect.y - t.pos()[1]))
            t.pensize(10)
            t.forward(rect.width)
            t.left(90)
            t.forward(rect.height)
            t.left(90)
            t.forward(rect.width)
            t.left(90)
            t.forward(rect.height)
            t.left(90)
            t.end_fill()

        time.sleep(5)
