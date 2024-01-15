#!/usr/bin/python3
"""Module for testing Rectangle class"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
import io
import os
import unittest.mock


class TestRectangle(unittest.TestCase):
    """
    Unit tests for the Rectangle class and its methods.
    """

    def setUp(self):
        """
        Runs before each test method.
        Reset the shared counter for the number of objects.
        """
        Base._Base__nb_objects = 0

    def test_instance_creation(self):
        """
        Test creating an instance of Rectangle.
        """
        r = Rectangle(10, 5)
        self.assertIsInstance(r, Rectangle)
        self.assertIsInstance(r, Base)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_custom_id(self):
        """
        Test creating an instance of Rectangle with a custom id.
        """
        r = Rectangle(10, 5, 1, 2, 100)
        self.assertEqual(r.id, 100)

    def test_property_setters(self):
        """
        Test property setters.
        """
        r = Rectangle(10, 5)
        r.width = 15
        r.height = 8
        r.x = 2
        r.y = 3
        self.assertEqual(r.width, 15)
        self.assertEqual(r.height, 8)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)

    def test_area(self):
        """
        Test area method.
        """
        r = Rectangle(10, 5)
        self.assertEqual(r.area(), 50)

    def test_display(self):
        """
        Test display method.
        """
        r = Rectangle(3, 2, 1, 1)
        with unittest.mock.patch(
                'sys.stdout', new_callable=io.StringIO
                ) as mock_stdout:
            r.display()
            self.assertEqual(
                    mock_stdout.getvalue(),
                    '\n ###\n ###\n'
                    )

            def test_str_representation(self):
                """
        Test __str__ method.
        """
        r = Rectangle(10, 5, 2, 1, 5)
        self.assertEqual(
                str(r),
                "[Rectangle] (5) 2/1 - 10/5"
                )

        def test_update_method(self):
            """
        Test update method.
        """
        r = Rectangle(10, 5, 2, 1, 5)
        r.update(1, 20, 10, 3, 2)
        self.assertEqual(
                str(r),
                "[Rectangle] (1) 3/2 - 20/10"
                )

        def test_update_method_kwargs(self):
            """
        Test update method with keyword arguments.
        """
        r = Rectangle(10, 5, 2, 1, 5)
        r.update(id=1, width=20, height=10, x=3, y=2)
        self.assertEqual(
                str(r),
                "[Rectangle] (1) 3/2 - 20/10"
                )

        def test_to_dictionary_method(self):
            """
        Test to_dictionary method.
        """
        r = Rectangle(10, 5, 2, 1, 5)
        expected_dict = {
                'id': 5,
                'width': 10,
                'height': 5,
                'x': 2,
                'y': 1
                }
        self.assertEqual(
                r.to_dictionary(),
                expected_dict
                )

        # Add more test methods for other functions in the Rectangle class

    def tearDown(self):
        """
        Runs after each test method.
        Remove created files if they exist.
        """
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")


if __name__ == '__main__':
    unittest.main()
