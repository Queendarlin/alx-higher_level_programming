#!/usr/bin/python3
"""Module for testing Base class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class TestBase(unittest.TestCase):
    """
    Unit tests for the Base class and its methods.
    """

    def setUp(self):
        """
        Runs before each test method.
        Reset the shared counter for the number of objects.
        """
        Base._Base__nb_objects = 0

    def test_instance_creation(self):
        """
        Test creating an instance of Base.
        """
        b = Base()
        self.assertIsInstance(b, Base)
        self.assertEqual(b.id, 1)

    def test_custom_id(self):
        """
        Test creating an instance of Base with a custom id.
        """
        b = Base(100)
        self.assertEqual(b.id, 100)

    def test_to_json_string(self):
        """
        Test to_json_string method.
        """
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(
                Base.to_json_string([{'key': 'value'}]),
                '[{"key": "value"}]'
                )
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_from_json_string(self):
        """
        Test from_json_string method.
        """
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(
                Base.from_json_string('[{"key": "value"}]'),
                [{'key': 'value'}]
                )
        self.assertEqual(Base.from_json_string(None), [])

    def test_save_to_file(self):
        """
        Test save_to_file method.
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", "r") as file:
            content = file.read()
            self.assertIn('"width": 10', content)
            self.assertIn('"height": 7', content)

    # Add more test methods for other functions in the Base class

    def tearDown(self):
        """
        Runs after each test method.
        Remove created files if they exist.
        """
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.exists("Base.json"):
            os.remove("Base.json")


if __name__ == '__main__':
    unittest.main()
