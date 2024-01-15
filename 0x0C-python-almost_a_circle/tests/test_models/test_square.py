#!/usr/bin/python3
"""Module for testing Rectangle class"""
import unittest
from models.base import Base
from models.square import Square
from random import randrange
from contextlib import redirect_stdout
import io


class TestSquare(unittest.TestCase):
    """Tests the Square class."""

    def setUp(self):
        """Set up test environment by resetting the object counter."""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Clean up/tear down  after each test method."""
        pass
    # ----------------- Task 2 ------------------------

    def test_class_type(self):
        """Test if Square class has the correct type."""
        self.assertEqual(str(Square), "<class 'models.square.Square'>")

    def test_inheritance_from_base(self):
        """Test if the Square class inherits from the Base class."""
        self.assertTrue(issubclass(Square, Base))

    def test_constructor_signature_no_args(self):
        """Test constructor signature for Square with no arguments."""
        with self.assertRaises(TypeError) as error_context:
            square = Square()
        error_msg = "__init__() missing 1 required positional argument: 'size'"
        self.assertEqual(str(error_context.exception), error_msg)

    def test_constructor_signature_many_args(self):
        """Test constructor signature for Square with too many arguments."""
        with self.assertRaises(TypeError) as error_context:
            square = Square(1, 2, 3, 4, 5)
        error_msg = "__init__() takes from 2 to 5 positional arguments but \
                6 were given"
        self.assertEqual(str(error_context.exception), error_msg)

    def test_square_instantiation(self):
        """Test instantiation of Square."""
        square = Square(10)
        self.assertEqual(str(type(square)), "<class 'models.square.Square'>")
        self.assertTrue(isinstance(square, Base))
        square_attributes = {'_Rectangle__height': 10, '_Rectangle__width': 10,
                             '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 1}
        self.assertDictEqual(square.__dict__, square_attributes)

        with self.assertRaises(TypeError) as error_context:
            square = Square("3")
        error_msg = "width must be an integer"
        self.assertEqual(str(error_context.exception), error_msg)

        with self.assertRaises(TypeError) as error_context:
            square = Square(1, "5")
        error_msg = "x must be an integer"
        self.assertEqual(str(error_context.exception), error_msg)

        with self.assertRaises(TypeError) as error_context:
            square = Square(1, 2, "4")
        error_msg = "y must be an integer"
        self.assertEqual(str(error_context.exception), error_msg)

        with self.assertRaises(ValueError) as error_context:
            square = Square(-4)
        error_msg = "width must be > 0"
        self.assertEqual(str(error_context.exception), error_msg)

        with self.assertRaises(ValueError) as error_context:
            square = Square(1, -3)
        error_msg = "x must be >= 0"
        self.assertEqual(str(error_context.exception), error_msg)

        with self.assertRaises(ValueError) as error_context:
            square = Square(1, 2, -5)
        error_msg = "y must be >= 0"
        self.assertEqual(str(error_context.exception), error_msg)

        with self.assertRaises(ValueError) as error_context:
            square = Square(0)
        error_msg = "width must be > 0"
        self.assertEqual(str(error_context.exception), error_msg)

    def test_positional_instantiation(self):
        """Test positional instantiation of Square."""
        square = Square(6, 15, 20)
        square_attributes = {'_Rectangle__height': 6, '_Rectangle__width': 6,
                             '_Rectangle__x': 15, '_Rectangle__y': 20, 'id': 1}
        self.assertDictEqual(square.__dict__, square_attributes)

        square = Square(3, 7, 8, 9)
        square_attributes = {'_Rectangle__height': 3, '_Rectangle__width': 3,
                             '_Rectangle__x': 7, '_Rectangle__y': 8, 'id': 9}
        self.assertDictEqual(square.__dict__, square_attributes)

    def test_keyword_instantiation(self):
        """Test keyword instantiation of Square."""
        square = Square(120, id=400, y=100, x=105)
        square_attr = {'_Rectangle__height': 120, '_Rectangle__width': 120,
                       '_Rectangle__x': 105, '_Rectangle__y': 100, 'id': 400}
        self.assertDictEqual(square.__dict__, square_attr)

    def test_id_inherited_from_base(self):
        """Test if id is inherited from Base."""
        Base._Base__nb_objects = 98
        square = Square(2)
        self.assertEqual(square.id, 99)

    def test_properties_getters_and_setters(self):
        """Test property getters and setters for Square."""
        square = Square(10, 20)
        square.size = 90
        square.x = 100
        square.y = 105
        square_attributes = {'_Rectangle__height': 90, '_Rectangle__width': 90,
                             '_Rectangle__x': 100, '_Rectangle__y': 105,
                             'id': 1}
        self.assertEqual(square.__dict__, square_attributes)
        self.assertEqual(square.size, 90)
        self.assertEqual(square.x, 100)
        self.assertEqual(square.y, 105)

    # ----------------- Task 3 ------------------------
    def invalid_types_for_validation(self):
        """Returns a tuple of invalid types for validation."""
        invalid_types = (3.14, -1.1, float('inf'), float('-inf'), True, "str",
                         (2,), [4], {5}, {6: 7}, None)
        return invalid_types

    def test_validate_type(self):
        """Tests property validation for Square."""
        square_instance = Square(1)
        attributes_to_test = ["x", "y"]
        for attr in attributes_to_test:
            error_message = "{} must be an integer".format(attr)
            for invalid_type in self.invalid_types_for_validation():
                with self.assertRaises(TypeError) as error_context:
                    setattr(square_instance, attr, invalid_type)
                self.assertEqual(str(error_context.exception), error_message)
        error_message = "width must be an integer"
        for invalid_type in self.invalid_types_for_validation():
            with self.assertRaises(TypeError) as error_context:
                setattr(square_instance, "width", invalid_type)
            self.assertEqual(str(error_context.exception), error_message)

    def test_validate_value_for_negative_gtd(self):
        """Tests property validation for Square."""
        square_instance = Square(1, 2)
        attributes_to_test = ["size"]
        for attr in attributes_to_test:
            error_message = "width must be > 0".format(attr)
            with self.assertRaises(ValueError) as error_context:
                setattr(square_instance, attr, -(randrange(10) + 1))
            self.assertEqual(str(error_context.exception), error_message)

    def test_validate_value_equal_negative_gtd(self):
        """Tests property validation for Square."""
        square_instance = Square(1, 2)
        attributes_to_test = ["x", "y"]
        for attribute in attributes_to_test:
            error_message = "{} must be >= 0".format(attribute)
            with self.assertRaises(ValueError) as error_context:
                setattr(square_instance, attribute, -(randrange(10) + 1))
            self.assertEqual(str(error_context.exception), error_message)

    def test_validate_value_for_zero(self):
        """Tests property validation for Square."""
        square_instance = Square(1, 2)
        attributes_to_test = ["size"]
        for attribute in attributes_to_test:
            error_message = "width must be > 0".format(attribute)
            with self.assertRaises(ValueError) as error_context:
                setattr(square_instance, attribute, 0)
            self.assertEqual(str(error_context.exception), error_message)

    def test_property_setting_and_getting(self):
        """Tests setting and getting properties for Square."""
        square_instance = Square(1, 2)
        attributes_to_test = ["x", "y", "width", "height"]
        for attribute in attributes_to_test:
            random_value = randrange(10) + 1
            setattr(square_instance, attribute, random_value)
            self.assertEqual(getattr(square_instance, attribute), random_value)

    def test_property_setting_and_getting_range_zero(self):
        """Tests setting and getting properties for Square with zero values."""
        square_instance = Square(1, 2)
        square_instance.x = 0
        square_instance.y = 0
        self.assertEqual(square_instance.x, 0)
        self.assertEqual(square_instance.y, 0)

    # ----------------- Task 4 ------------------------
    def test_area_method_signature(self):
        """Tests area() method signature for Square."""
        square_instance = Square(5)
        with self.assertRaises(TypeError) as error_context:
            Square.area()
        error_msg = "area() missing 1 required positional argument: 'self'"
        self.assertEqual(str(error_context.exception), error_msg)

    def test_area_computation(self):
        """Tests area() method computation for Square."""
        square_instance = Square(6)
        self.assertEqual(square_instance.area(), 36)
        random_size = randrange(10) + 1
        square_instance.size = random_size
        self.assertEqual(square_instance.area(), random_size * random_size)
        random_size = randrange(10) + 1
        square_instance = Square(random_size, 7, 8, 9)
        self.assertEqual(square_instance.area(), random_size * random_size)
        random_size = randrange(10) + 1
        square_instance = Square(random_size, y=7, x=8, id=9)
        self.assertEqual(square_instance.area(), random_size * random_size)

        Base._Base__nb_objects = 0
        square1 = Square(5)
        self.assertEqual(str(square1), "[Square] (1) 0/0 - 5")
        self.assertEqual(square1.size, 5)
        square1.size = 10
        self.assertEqual(str(square1), "[Square] (1) 0/0 - 10")
        self.assertEqual(square1.size, 10)

        with self.assertRaises(TypeError) as error_context:
            square1.size = "9"
        self.assertEqual(str(error_context.exception),
                         "width must be an integer")

        with self.assertRaises(ValueError) as error_context:
            square1.size = 0
        self.assertEqual(str(error_context.exception), "width must be > 0")

    # ----------------- Task 5 and 7 ------------------------
    def test_display_method_signature(self):
        """Tests display() method signature for Square."""
        square_instance = Square(9)
        with self.assertRaises(TypeError) as error_context:
            Square.display()
        error_msg = "display() missing 1 required positional argument: 'self'"
        self.assertEqual(str(error_context.exception), error_msg)

    def test_display_output(self):
        """Tests display() method with different configurations for Square."""
        square_instance = Square(1)
        output_buffer = io.StringIO()
        with redirect_stdout(output_buffer):
            square_instance.display()
        expected_output = "#\n"
        self.assertEqual(output_buffer.getvalue(), expected_output)

        square_instance.size = 3
        output_buffer = io.StringIO()
        with redirect_stdout(output_buffer):
            square_instance.display()
        expected_output = "\
###\n\
###\n\
###\n\
"
        self.assertEqual(output_buffer.getvalue(), expected_output)

        square_instance = Square(5, 6, 7)
        output_buffer = io.StringIO()
        with redirect_stdout(output_buffer):
            square_instance.display()
        expected_output = """\







      #####
      #####
      #####
      #####
      #####
"""
        self.assertEqual(output_buffer.getvalue(), expected_output)
        square_instance = Square(9, 8)
        output_buffer = io.StringIO()
        with redirect_stdout(output_buffer):
            square_instance.display()
        expected_output = """\
        #########
        #########
        #########
        #########
        #########
        #########
        #########
        #########
        #########
"""
        self.assertEqual(output_buffer.getvalue(), expected_output)
        square_instance = Square(1, 1, 10)
        output_buffer = io.StringIO()
        with redirect_stdout(output_buffer):
            square_instance.display()
        expected_output = """\










 #
"""
        self.assertEqual(output_buffer.getvalue(), expected_output)

        square_instance = Square(5)
        output_buffer = io.StringIO()
        with redirect_stdout(output_buffer):
            square_instance.display()
        expected_output = """ \
#####
#####
#####
#####
#####
"""
        self.assertEqual(output_buffer.getvalue(), expected_output)

        # Test case for Square(5, 5)
        square_instance = Square(5, 5)
        output_buffer = io.StringIO()
        with redirect_stdout(output_buffer):
            square_instance.display()
        expected_output = """ \
     #####
     #####
     #####
     #####
     #####
"""
        self.assertEqual(output_buffer.getvalue(), expected_output)

        # Test case for Square(5, 3)
        square_instance = Square(5, 3)
        output_buffer = io.StringIO()
        with redirect_stdout(output_buffer):
            square_instance.display()
        expected_output = """\
   #####
   #####
   #####
   #####
   #####
"""
        self.assertEqual(output_buffer.getvalue(), expected_output)

        # Test case for Square(5, 0, 4)
        square_instance = Square(5, 0, 4)
        output_buffer = io.StringIO()
        with redirect_stdout(output_buffer):
            square_instance.display()
        expected_output = """\




#####
#####
#####
#####
#####
"""
        self.assertEqual(output_buffer.getvalue(), expected_output)

        # Test case for Square(5)
        Base._Base__nb_objects = 0
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        self.assertEqual(s1.area(), 25)
        output_buffer = io.StringIO()
        with redirect_stdout(output_buffer):
            s1.display()
        expected_output = """\
#####
#####
#####
#####
#####
"""
        self.assertEqual(output_buffer.getvalue(), expected_output)

        s3 = Square(3, 1, 3)
        self.assertEqual(str(s3), "[Square] (3) 1/3 - 3")
        self.assertEqual(s3.area(), 9)
        output_buffer = io.StringIO()
        with redirect_stdout(output_buffer):
            s3.display()
        expected_output = """\
  ##
  ##
"""
        self.assertEqual(output_buffer.getvalue(), expected_output)

    # ----------------- Task 6 ------------------------
    def test_str_signature_no_args(self):
        """Tests __str__() method with no argument."""
        square_instance = Square(5, 2)
        with self.assertRaises(TypeError) as error_context:
            square_instance.__str__()
        error_msg = "__str__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(error_context.exception), error_msg)

    def test_str_representation(self):
        """Tests __str__() method return."""
        # Test case for Square(5)
        square_instance = Square(5)
        expected_output = '[Square] (1) 0/0 - 5'
        self.assertEqual(str(square_instance), expected_output)

        # Test case for Square(1, 1)
        square_instance = Square(1, 1)
        expected_output = '[Square] (2) 1/0 - 1'
        self.assertEqual(str(square_instance), expected_output)

        # Test case for Square(3, 4, 5)
        square_instance = Square(3, 4, 5)
        expected_output = '[Square] (3) 4/5 - 3'
        self.assertEqual(str(square_instance), expected_output)

        # Test case for Square(10, 20, 30, 40)
        square_instance = Square(10, 20, 30, 40)
        expected_output = '[Square] (40) 20/30 - 10'
        self.assertEqual(str(square_instance), expected_output)

    # ----------------- Task 8 and 9 ------------------------
    def test_update_signature_with_no_argument(self):
        """Tests the update() method with no argument."""
        square_instance = Square(5, 2)
        with self.assertRaises(TypeError) as error_context:
            square_instance.update()
        error_msg = "update() missing 1 required positional argument: 'self'"
        self.assertEqual(str(error_context.exception), error_msg)

        instance_dict = square_instance.__dict__.copy()
        square_instance.update()
        self.assertEqual(square_instance.__dict__, instance_dict)

    def test_update_positional_args(self):
        """Tests update() with positional args."""
        square_instance = Square(5, 2)
        instance_dict = square_instance.__dict__.copy()

        square_instance.update(10)
        instance_dict["id"] = 10
        self.assertEqual(square_instance.__dict__, instance_dict)

        square_instance.update(10, 5)
        instance_dict["_Rectangle__height"] = 5
        instance_dict["_Rectangle__width"] = 5
        self.assertEqual(square_instance.__dict__, instance_dict)

        square_instance.update(10, 5, 20)
        instance_dict["_Rectangle__x"] = 20
        self.assertEqual(square_instance.__dict__, instance_dict)

        square_instance.update(10, 5, 20, 25)
        instance_dict["_Rectangle__y"] = 25
        self.assertEqual(square_instance.__dict__, instance_dict)

    def test_update_invalid_args(self):
        """Tests update() invalid positional args."""
        square_instance = Square(5, 2)
        instance_dict = square_instance.__dict__.copy()

        square_instance.update(10)
        instance_dict["id"] = 10
        self.assertEqual(square_instance.__dict__, instance_dict)

        with self.assertRaises(ValueError) as error_context:
            square_instance.update(10, -5)
        error_message = "width must be > 0"
        self.assertEqual(str(error_context.exception), error_message)

        with self.assertRaises(ValueError) as error_context:
            square_instance.update(10, 5, -17)
        error_message = "x must be >= 0"
        self.assertEqual(str(error_context.exception), error_message)

        with self.assertRaises(ValueError) as error_context:
            square_instance.update(10, 5, 17, -25)
        error_message = "y must be >= 0"
        self.assertEqual(str(error_context.exception), error_message)

    def test_update_keyword_args(self):
        """Tests update() with keyword args."""
        square_instance = Square(5, 2)
        instance_dict = square_instance.__dict__.copy()

        square_instance.update(id=10)
        instance_dict["id"] = 10
        self.assertEqual(square_instance.__dict__, instance_dict)

        square_instance.update(size=17)
        instance_dict["_Rectangle__height"] = 17
        instance_dict["_Rectangle__width"] = 17
        self.assertEqual(square_instance.__dict__, instance_dict)

        square_instance.update(x=20)
        instance_dict["_Rectangle__x"] = 20
        self.assertEqual(square_instance.__dict__, instance_dict)

        square_instance.update(y=25)
        instance_dict["_Rectangle__y"] = 25
        self.assertEqual(square_instance.__dict__, instance_dict)

    def test_more_update_keyword_args(self):
        """Tests update() keyword args."""
        square_instance = Square(5, 2)
        instance_dict = square_instance.__dict__.copy()

        square_instance.update(id=10)
        instance_dict["id"] = 10
        self.assertEqual(square_instance.__dict__, instance_dict)

        square_instance.update(id=10, size=5)
        instance_dict["_Rectangle__height"] = 5
        instance_dict["_Rectangle__width"] = 5
        self.assertEqual(square_instance.__dict__, instance_dict)

        square_instance.update(id=10, size=5, x=20)
        instance_dict["_Rectangle__x"] = 20
        self.assertEqual(square_instance.__dict__, instance_dict)

        square_instance.update(id=10, size=5, x=20, y=25)
        instance_dict["_Rectangle__y"] = 25
        self.assertEqual(square_instance.__dict__, instance_dict)

        square_instance.update(y=25, id=10, x=20, size=5)
        self.assertEqual(square_instance.__dict__, instance_dict)

        Base._Base__nb_objects = 0
        square1 = Square(5)
        self.assertEqual(str(square1), "[Square] (1) 0/0 - 5")

        square1.update(10)
        self.assertEqual(str(square1), "[Square] (10) 0/0 - 5")

        square1.update(1, 2)
        self.assertEqual(str(square1), "[Square] (1) 0/0 - 2")

        square1.update(1, 2, 3)
        self.assertEqual(str(square1), "[Square] (1) 3/0 - 2")

        square1.update(1, 2, 3, 4)
        self.assertEqual(str(square1), "[Square] (1) 3/4 - 2")

        square1.update(x=12)
        self.assertEqual(str(square1), "[Square] (1) 12/4 - 2")

        square1.update(size=7, y=1)
        self.assertEqual(str(square1), "[Square] (1) 12/1 - 7")

        square1.update(size=7, id=89, y=1)
        self.assertEqual(str(square1), "[Square] (89) 12/1 - 7")

    def test_to_dictionary(self):
        """Tests to_dictionary() method with various scenarios."""
        # Check if to_dictionary() raises TypeError without self argument
        with self.assertRaises(TypeError) as error_context:
            Square.to_dictionary()
        error_msg = "to_dictionary() missing 1 required positional argument: \
'self'"
        self.assertEqual(str(error_context.exception), error_msg)

        # Test to_dictionary() with a Square instance
        square = Square(1)
        expected_dict = {'x': 0, 'y': 0, 'size': 1, 'id': 1}
        self.assertEqual(square.to_dictionary(), expected_dict)

        # Test to_dictionary() with a Square instance with specified values
        square = Square(9, 2, 3, 4)
        expected_dict = {'x': 2, 'y': 3, 'size': 9, 'id': 4}
        self.assertEqual(square.to_dictionary(), expected_dict)

        # Test to_dictionary() after modifying attributes
        square.x = 10
        square.y = 20
        square.size = 30
        expected_dict = {'x': 10, 'y': 20, 'size': 30, 'id': 4}
        self.assertEqual(square.to_dictionary(), expected_dict)

        # Test if updating another Square with the dictionary representation
        square1 = Square(10, 2, 1)
        square1_dict = square1.to_dictionary()
        square2 = Square(1, 1)
        square2.update(**square1_dict)
        self.assertEqual(str(square1), str(square2))
        self.assertNotEqual(square1, square2)


if __name__ == "__main__":
    unittest.main()
