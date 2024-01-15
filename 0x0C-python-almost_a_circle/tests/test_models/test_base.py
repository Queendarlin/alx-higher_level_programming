#!/usr/bin/python3
"""Module for testing Base class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def setUp(self):
        """
        Set up the environment before each test.
        Resets the private class attribute __nb_objects to 0.
        """
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        """
        Tear down/clean up the environment after each test.
        Doesn't have any specific functionality for now.
        It's a placeholder for any future cleanup steps.
        """
        pass

    def test_private_nb_objects_(self):
        """Checks whether the Base class has a private class attribute
        named __nb_objects.
        """
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_initialization_nb_objects(self):
        """Ensures the __nb_objects attribute of the Base class
        is initialized to zero.
        """
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)

    def test_instantiation_class(self):
        """This test checks if the Base class can be instantiated correctly,
        and if the attributes are set as expected.
        """
        base_inst = Base()
        self.assertEqual(str(type(base_inst)), "<class 'models.base.Base'>")
        self.assertEqual(base_inst.__dict__, {"id": 1})
        self.assertEqual(base_inst.id, 1)

    def test_constructor_signature(self):
        """Ensures that calling the __init__ method without arguments
                raises the expected TypeError"""
        with self.assertRaises(TypeError) as error_context:
            Base.__init__()
        err_msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(error_context.exception), err_msg)

    def test_2_args_constructor(self):
        """Ensures that calling the __init__ method with 2 arguments
        raises the expected TypeError."""
        with self.assertRaises(TypeError) as error_context:
            Base.__init__(self, 1, 2)
        m = "__init__() takes from 1 to 2 positional arguments but 3 \
were given"
        self.assertEqual(str(error_context.exception), m)

    def test_consecutive_ids(self):
        """checks if the ids generated by the Base class are consecutive."""
        base_object1 = Base()
        base_object2 = Base()
        self.assertEqual(base_object1.id + 1, base_object2.id)

    def test_sync_class_instance_id(self):
        """checks if the nb_objects class attribute is synchronized
        with the id of the created instance"""
        base_obj = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), base_obj.id)

    def test_more_sync_class_instance_id(self):
        """checks if the nb_objects class attribute is synchronized
        with the id of multiple created instances"""
        base_obj = Base()
        base_obj = Base("Miss")
        base_obj = Base(98)
        base_obj = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), base_obj.id)

    def test_custom_int_id(self):
        """checks if a custom integer id
        is correctly set for the Base instance"""
        int_num = 98
        base_obj = Base(int_num)
        self.assertEqual(base_obj.id, int_num)

    def test_custom_str_id(self):
        """checks if a custom string id is correctly set"""
        str_string = "MissWorld"
        base_obj = Base(str_string)
        self.assertEqual(base_obj.id, str_string)

    def test_keyword_id(self):
        """checks if the id can be passed as a keyword argument
        when creating a Base instance."""
        int_num = 421
        base_obj = Base(id=int_num)
        self.assertEqual(base_obj.id, int_num)

    # JSON
    def test_to_json_string(self):
        """Tests the to_json_string() method's signature and functionality.

        Ensures that the to_json_string() method:
        - Raises a TypeError if called without 'list_dictionaries' argument
        - Produces the expected JSON string for different input scenarios.
        - Handles various types of input dictionaries, including custom cases.
        """
        with self.assertRaises(TypeError) as error_context:
            Base.to_json_string()
        error_message = "to_json_string() \
missing 1 required positional argument: 'list_dictionaries'"
        self.assertEqual(str(error_context.exception), error_message)

        self.assertEqual(Base.to_json_string(None), "[]")

        self.assertEqual(Base.to_json_string([]), "[]")

        dict_single = [{'x': 101, 'y': 20123, 'width': 312321,
                        'id': 522244, 'height': 34340}]
        self.assertEqual(len(Base.to_json_string(dict_single)),
                         len(str(dict_single)))

        dict_list = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5}]
        self.assertEqual(len(Base.to_json_string(dict_list)),
                         len(str(dict_list)))

        custom_dict = [{"foobarrooo": 989898}]
        self.assertEqual(Base.to_json_string(custom_dict),
                         '[{"foobarrooo": 989898}]')

        custom_dicts = [{"foobarrooo": 989898}, {"abc": 123}, {"HI": 0}]
        self.assertEqual(Base.to_json_string(custom_dicts),
                         '[{"foobarrooo": 989898}, {"abc": 123}, {"HI": 0}]')

        dict_list = [
            {'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5},
            {'x': 101, 'y': 20123, 'width': 312321, 'id': 522244,
             'height': 34340}
        ]
        self.assertEqual(len(Base.to_json_string(dict_list)),
                         len(str(dict_list)))

        dict_empty = [{}]
        self.assertEqual(Base.to_json_string(dict_empty), '[{}]')

        dict_multiple_empty = [{}, {}]
        self.assertEqual(Base.to_json_string(dict_multiple_empty), '[{}, {}]')

        rectangle1 = Rectangle(10, 7, 2, 8)
        dict_rect1 = rectangle1.to_dictionary()
        json_dict_rect1 = Base.to_json_string([dict_rect1])
        dict_str_rect1 = str([dict_rect1]).replace("'", '"')
        self.assertEqual(dict_str_rect1, json_dict_rect1)

        rectangle1 = Rectangle(10, 7, 2, 8)
        rectangle2 = Rectangle(1, 2, 3, 4)
        rectangle3 = Rectangle(2, 3, 4, 5)
        dict_rectangles = [rectangle1.to_dictionary(),
                           rectangle2.to_dictionary(),
                           rectangle3.to_dictionary()]
        json_dict_rectangles = Base.to_json_string(dict_rectangles)
        dict_str_rectangles = str(dict_rectangles).replace("'", '"')
        self.assertEqual(dict_str_rectangles, json_dict_rectangles)

        square1 = Square(10, 7, 2)
        dict_square1 = square1.to_dictionary()
        json_dict_square1 = Base.to_json_string([dict_square1])
        dict_str_square1 = str([dict_square1]).replace("'", '"')
        self.assertEqual(dict_str_square1, json_dict_square1)

        square1 = Square(10, 7, 2)
        square2 = Square(1, 2, 3)
        square3 = Square(2, 3, 4)
        dict_squares = [square1.to_dictionary(), square2.to_dictionary(),
                        square3.to_dictionary()]
        json_dict_squares = Base.to_json_string(dict_squares)
        dict_str_squares = str(dict_squares).replace("'", '"')
        self.assertEqual(dict_str_squares, json_dict_squares)

    def test_from_json_string(self):
        """Tests the from_json_string() method's signature and functionality.

        Ensures that the from_json_string() method:
        Raises a TypeError if called without the required json_string argument
        Returns an empty list when provided with None or an empty string.
        Converts a JSON string to a list of dictionaries for various input.
        Converts dictionaries from Rectangle instances to the correct format.
        Handles conversion for both Rectangle and Square classes.
        """
        with self.assertRaises(TypeError) as error_context:
            Base.from_json_string()
        error_message = "from_json_string() missing 1 required positional \
argument: 'json_string'"
        self.assertEqual(str(error_context.exception), error_message)

        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])

        json_string = ('[{"x": 1, "y": 2, "width": 3, "id": 4, "height": 5}, \
                       {"x": 101, "y": 20123, "width": 312321, "id": 522244,'
                       '"height": 34340}]')
        expected_output = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5},
                           {'x': 101, 'y': 20123, 'width': 312321,
                            'id': 522244, 'height': 34340}]
        self.assertEqual(Base.from_json_string(json_string), expected_output)

        expected_output = [{}, {}]
        json_string = '[{}, {}]'
        self.assertEqual(Base.from_json_string(json_string), expected_output)
        expected_output = [{}]
        json_string = '[{}]'
        self.assertEqual(Base.from_json_string(json_string), expected_output)

        expected_output = [{"foobarrooo": 989898}, {"abc": 123}, {"HI": 0}]
        json_string = '[{"foobarrooo": 989898}, {"abc": 123}, {"HI": 0}]'
        self.assertEqual(Base.from_json_string(json_string), expected_output)

        expected_output = [{"foobarrooo": 989898}]
        json_string = '[{"foobarrooo": 989898}]'
        self.assertEqual(Base.from_json_string(json_string), expected_output)

        json_string_1 = '[{"x": 1, "y": 2, "width": 3, "id": 4, "height": 5}]'
        expected_output_1 = [{'x': 1, 'y': 2, 'width': 3, 'id': 4,
                              'height': 5}]
        self.assertEqual(Base.from_json_string(json_string_1),
                         expected_output_1)

        json_string_2 = ('[{"x": 101, "y": 20123, "width": 312321,'
                         '"id": 522244, "height": 34340}]')
        expected_output_2 = [{'x': 101, 'y': 20123, 'width': 312321,
                              'id': 522244, 'height': 34340}]
        self.assertEqual(Base.from_json_string(json_string_2),
                         expected_output_2)

        input_list = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        output_list = \
            Rectangle.from_json_string(Rectangle.to_json_string(input_list))
        self.assertEqual(input_list, output_list)


if __name__ == '__main__':
    unittest.main()
