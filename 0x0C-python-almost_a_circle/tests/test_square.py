#!/usr/bin/python3
"""Test case for Square class"""
import unittest
from models.square import Square
from models.base import Base
import io
import os
import unittest.mock


class TestSquare(unittest.TestCase):
    """
    Unit tests for the Square class and its methods.
    """

    def setUp(self):
        """
        Runs before each test method.
        Reset the shared counter for the number of objects.
        """
        Base._Base__nb_objects = 0

    def test_instance_creation(self):
        """
        Test creating an instance of Square.
        """
        s = Square(5)
        self.assertIsInstance(s, Square)
        self.assertIsInstance(s, Base)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_custom_id(self):
        """
        Test creating an instance of Square with a custom id.
        """
        s = Square(5, 1, 2, 100)
        self.assertEqual(s.id, 100)

    def test_property_setters(self):
        """
        Test property setters.
        """
        s = Square(5)
        s.size = 10
        s.x = 2
        s.y = 3
        self.assertEqual(s.size, 10)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_area(self):
        """
        Test area method.
        """
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_to_dictionary_method(self):
        """
        Test to_dictionary method.
        """
        s = Square(5, 2, 1, 5)
        expected_dict = {'id': 5, 'size': 5, 'x': 2, 'y': 1}
        self.assertEqual(s.to_dictionary(), expected_dict)

    # Add more test methods for other functions in the Square class

    def tearDown(self):
        """
        Runs after each test method.
        Remove created files if they exist.
        """
        if os.path.exists("Square.json"):
            os.remove("Square.json")


if __name__ == '__main__':
    unittest.main()
