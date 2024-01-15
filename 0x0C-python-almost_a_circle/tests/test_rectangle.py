#!/usr/bin/python3
"""Module for testing Rectangle class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from random import randrange
from contextlib import redirect_stdout
import io


class TestRectangle(unittest.TestCase):
    """Tests the Rectangle class."""

    def setUp(self):
        """Set up test environment by resetting the object counter."""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Clean up/tear down  after each test method."""
        pass

    # ----------------- Tests for #2 ------------------------

    def test_rectangle_class_type(self):
        """Test if Rectangle class has the correct type."""
        self.assertEqual(str(Rectangle),
                         "<class 'models.rectangle.Rectangle'>")

    def test_inheritance_from_base(self):
        """Test if Rectangle inherits from Base class."""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_constructor_no_args(self):
        """Test the constructor signature without arguments."""
        with self.assertRaises(TypeError) as error_context:
            rectangle = Rectangle()
        error_message = "__init__() missing 2 required positional arguments: \
'width' and 'height'"
        self.assertEqual(str(error_context.exception), error_message)

    def test_constructor_with_too_many_args(self):
        """Tests constructor signature with too many arguments."""
        with self.assertRaises(TypeError) as error_context:
            rectangle_instance = Rectangle(1, 2, 3, 4, 5, 6)
        error_message = "__init__() takes from 3 to 6 positional arguments \
but 7 were given"
        self.assertEqual(str(error_context.exception), error_message)

    def test_constructor_with_one_arg(self):
        """Tests constructor signature with only one argument."""
        with self.assertRaises(TypeError) as error_context:
            rectangle_instance = Rectangle(1)
        error_message = "__init__() missing 1 required positional argument: \
'height'"
        self.assertEqual(str(error_context.exception), error_message)

    def test_instantiation_and_validation(self):
        """Tests instantiation and validation of Rectangle attributes."""
        # Valid instantiation
        rectangle_instance = Rectangle(10, 20)
        self.assertEqual(str(type(rectangle_instance)),
                         "<class 'models.rectangle.Rectangle'>")
        self.assertTrue(isinstance(rectangle_instance, Base))
        expected_dict = {'_Rectangle__height': 20, '_Rectangle__width': 10,
                         '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 1}
        self.assertDictEqual(rectangle_instance.__dict__, expected_dict)

        # Invalid instantiation with non-integer values
        with self.assertRaises(TypeError) as error_context:
            rectangle_instance = Rectangle("1", 2)
        self.assertEqual(str(error_context.exception),
                         "width must be an integer")

        with self.assertRaises(TypeError) as error_context:
            rectangle_instance = Rectangle(1, "2")
        self.assertEqual(str(error_context.exception),
                         "height must be an integer")

        with self.assertRaises(TypeError) as error_context:
            rectangle_instance = Rectangle(1, 2, "3")
        self.assertEqual(str(error_context.exception), "x must be an integer")

        with self.assertRaises(TypeError) as error_context:
            rectangle_instance = Rectangle(1, 2, 3, "4")
        self.assertEqual(str(error_context.exception), "y must be an integer")

        # Invalid instantiation with non-positive values
        with self.assertRaises(ValueError) as error_context:
            rectangle_instance = Rectangle(-1, 2)
        self.assertEqual(str(error_context.exception), "width must be > 0")

        with self.assertRaises(ValueError) as error_context:
            rectangle_instance = Rectangle(1, -2)
        self.assertEqual(str(error_context.exception), "height must be > 0")

        with self.assertRaises(ValueError) as error_context:
            rectangle_instance = Rectangle(0, 2)
        self.assertEqual(str(error_context.exception), "width must be > 0")

        with self.assertRaises(ValueError) as error_context:
            rectangle_instance = Rectangle(1, 0)
        self.assertEqual(str(error_context.exception), "height must be > 0")

        with self.assertRaises(ValueError) as error_context:
            rectangle_instance = Rectangle(1, 2, -3)
        self.assertEqual(str(error_context.exception), "x must be >= 0")

        with self.assertRaises(ValueError) as error_context:
            rectangle_instance = Rectangle(1, 2, 3, -4)
        self.assertEqual(str(error_context.exception), "y must be >= 0")

    def test_instantiation_with_positional_args(self):
        """Tests positional instantiation of Rectangle."""
        rectangle_instance = Rectangle(5, 10, 15, 20)
        expected_dict = {'_Rectangle__height': 10, '_Rectangle__width': 5,
                         '_Rectangle__x': 15, '_Rectangle__y': 20, 'id': 1}
        self.assertEqual(rectangle_instance.__dict__, expected_dict)

        rectangle_instance = Rectangle(5, 10, 15, 20, 98)
        expected_dict = {'_Rectangle__height': 10, '_Rectangle__width': 5,
                         '_Rectangle__x': 15, '_Rectangle__y': 20, 'id': 98}
        self.assertEqual(rectangle_instance.__dict__, expected_dict)

    def test_instantiation_with_keyword_args(self):
        """Tests keyword instantiation of Rectangle."""
        rectangle_instance = Rectangle(100, 200, id=421, y=99, x=101)
        expected_dict = {'_Rectangle__height': 200, '_Rectangle__width': 100,
                         '_Rectangle__x': 101, '_Rectangle__y': 99, 'id': 421}
        self.assertEqual(rectangle_instance.__dict__, expected_dict)

    def test_inherited_id_from_base(self):
        """Tests whether id is inherited from the Base class."""
        Base._Base__nb_objects = 98
        rectangle_instance = Rectangle(2, 4)
        self.assertEqual(rectangle_instance.id, 99)

    def test_property_getters_setters(self):
        """Tests property getters and setters of Rectangle."""
        # Create a Rectangle instance
        rectangle_instance = Rectangle(8, 12)

        # Modify attributes using setters
        rectangle_instance.width = 88
        rectangle_instance.height = 99
        rectangle_instance.x = 77
        rectangle_instance.y = 66

        # Expected dictionary after modifications
        expected_dict = {'_Rectangle__height': 99, '_Rectangle__width': 88,
                         '_Rectangle__x': 77, '_Rectangle__y': 66, 'id': 1}

        # Check if the instance dictionary matches the expected dictionary
        self.assertEqual(rectangle_instance.__dict__, expected_dict)

        # Check if getters return the expected values
        self.assertEqual(rectangle_instance.width, 88)
        self.assertEqual(rectangle_instance.height, 99)
        self.assertEqual(rectangle_instance.x, 77)
        self.assertEqual(rectangle_instance.y, 66)

    # ----------------- Task 3 ------------------------
    def invalid_types_check(self):
        """
        Returns a tuple of invalid types for property validation.
        """
        invalid_types = (3.14, -1.1, float('inf'), float('-inf'),
                         True, "str", (2,), [4], {5}, {6: 7}, None)
        return invalid_types

    def test_validate_type(self):
        """
        Tests property type validation for Rectangle attributes.
        """
        rectangle_instance = Rectangle(1, 2)
        attributes = ["x", "y", "width", "height"]

        for attr in attributes:
            error_message = "{} must be an integer".format(attr)

            for invalid_types in self.invalid_types_check():
                with self.assertRaises(TypeError) as error_context:
                    setattr(rectangle_instance, attr, invalid_types)
                self.assertEqual(str(error_context.exception), error_message)

    def test_validate_property_value_gtd_negative(self):
        """
        Tests property value validation
        (negative and greater than) for Rectangle attributes.
        """
        rectangle_instance = Rectangle(1, 2)
        attributes = ["width", "height"]

        for attr in attributes:
            error_message = "{} must be > 0".format(attr)
            with self.assertRaises(ValueError) as error_context:
                setattr(rectangle_instance, attr, -(randrange(10) + 1))
            self.assertEqual(str(error_context.exception), error_message)

    def test_validate_value_equal_negative_gtd(self):
        """
        Tests property value validation (negative and greater than or equal)
        for Rectangle attributes.
        """
        rectangle_instance = Rectangle(1, 2)
        attributes = ["x", "y"]
        for attr in attributes:
            error_message = "{} must be >= 0".format(attr)
            with self.assertRaises(ValueError) as error_context:
                setattr(rectangle_instance, attr, -(randrange(10) + 1))
            self.assertEqual(str(error_context.exception), error_message)

    def test_zero_value_validation(self):
        """
        Tests property value validation (zero) for Rectangle attributes.
        """
        rectangle_instance = Rectangle(1, 2)
        attributes = ["width", "height"]
        for attr in attributes:
            error_message = "{} must be > 0".format(attr)
            with self.assertRaises(ValueError) as error_context:
                setattr(rectangle_instance, attr, 0)
            self.assertEqual(str(error_context.exception), error_message)

    def test_property_setting_and_getting(self):
        """
        Tests property setting and getting for Rectangle attributes.
        """
        rectangle_instance = Rectangle(1, 2)
        attributes = ["x", "y", "width", "height"]
        for attr in attributes:
            new_value = randrange(10) + 1
            setattr(rectangle_instance, attr, new_value)
            self.assertEqual(getattr(rectangle_instance, attr), new_value)

    def test_property_setting_getting_range_zero(self):
        """
        Tests property setting and getting for Rectangle attributes
        with a zero range.
        """
        rectangle_instance = Rectangle(1, 2)
        rectangle_instance.x = 0
        rectangle_instance.y = 0

        self.assertEqual(rectangle_instance.x, 0)
        self.assertEqual(rectangle_instance.y, 0)
    # ----------------- Task 4 ------------------------

    def test_area_with_no_args(self):
        """
        Tests the area() method signature when called without any arguments.

        This test ensures that calling the area() method without any arguments
        raises a TypeError with a specific error message.
        """
        rectangle_instance = Rectangle(5, 6)
        with self.assertRaises(TypeError) as error_context:
            Rectangle.area()
        error_msg = "area() missing 1 required positional argument: 'self'"
        self.assertEqual(str(error_context.exception), error_msg)

    def test_area(self):
        """
        Tests the computation of the area() method.

        This test verifies the correctness of the area() method
        by checking its output against expected values for various scenarios
        including different rectangle dimensions and instances.
        """
        rectangle_instance_1 = Rectangle(5, 6)
        self.assertEqual(rectangle_instance_1.area(), 30)
        width_1 = randrange(10) + 1
        height_1 = randrange(10) + 1
        rectangle_instance_1.width = width_1
        rectangle_instance_1.height = height_1
        self.assertEqual(rectangle_instance_1.area(), width_1 * height_1)

        width_2 = randrange(10) + 1
        height_2 = randrange(10) + 1
        rectangle_instance_2 = Rectangle(width_2, height_2, 7, 8, 9)
        self.assertEqual(rectangle_instance_2.area(), width_2 * height_2)

        width_3 = randrange(10) + 1
        height_3 = randrange(10) + 1
        rectangle_instance_3 = Rectangle(width_3, height_3, y=7, x=8, id=9)
        self.assertEqual(rectangle_instance_3.area(), width_3 * height_3)

        # Additional test cases
        rectangle_instance_4 = Rectangle(3, 2)
        self.assertEqual(rectangle_instance_4.area(), 6)

        rectangle_instance_5 = Rectangle(2, 10)
        self.assertEqual(rectangle_instance_5.area(), 20)

        rectangle_instance_6 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(rectangle_instance_6.area(), 56)

    # ----------------- Task 5 and 7 ------------------------

    def test_display_with_no_args(self):
        """
        Tests the display() method signature when called without any arguments

        Ensures that calling the display() method without any arguments
        raises a TypeError with a specific error message.
        """
        rectangle_instance = Rectangle(9, 8)
        with self.assertRaises(TypeError) as error_context:
            Rectangle.display()
        error_msg = "display() missing 1 required positional argument: 'self'"
        self.assertEqual(str(error_context.exception), error_msg)

    def test_display_rectangle_symbol(self):
        """
        Tests output of the display() method for many rectangle configurations

        This test verifies the correctness of the display() method
        by capturing its output and comparing it against expected string
        representations for various rectangle dimensions and positions.
        """
        # Test case 1
        rectangle_instance_1 = Rectangle(1, 1)
        f_1 = io.StringIO()
        with redirect_stdout(f_1):
            rectangle_instance_1.display()
        expected_output_1 = "#\n"
        self.assertEqual(f_1.getvalue(), expected_output_1)

        # Test case 2
        rectangle_instance_2 = Rectangle(3, 5)
        f_2 = io.StringIO()
        with redirect_stdout(f_2):
            rectangle_instance_2.display()
        expected_output_2 = "\
###\n\
###\n\
###\n\
###\n\
###\n\
"
        self.assertEqual(f_2.getvalue(), expected_output_2)

        # Test case 3
        rectangle_instance_3 = Rectangle(5, 6, 7, 8)
        f_3 = io.StringIO()
        with redirect_stdout(f_3):
            rectangle_instance_3.display()
        expected_output_3 = """







       #####
       #####
       #####
       #####
       #####
       #####
"""
        self.assertEqual(f_3.getvalue(), expected_output_3)

        # Additional test cases
        rectangle_instance_4 = Rectangle(9, 8)
        f_4 = io.StringIO()
        with redirect_stdout(f_4):
            rectangle_instance_4.display()
        expected_output_4 = """\
#########
#########
#########
#########
#########
#########
#########
#########
"""
        self.assertEqual(f_4.getvalue(), expected_output_4)

        rectangle_instance_5 = Rectangle(1, 1, 10, 10)
        f_5 = io.StringIO()
        with redirect_stdout(f_5):
            rectangle_instance_5.display()
        expected_output_5 = """\










          #
"""
        self.assertEqual(f_5.getvalue(), expected_output_5)

        rectangle_instance_6 = Rectangle(5, 5)
        f_6 = io.StringIO()
        with redirect_stdout(f_6):
            rectangle_instance_6.display()
        expected_output_6 = """\
#####
#####
#####
#####
#####
"""
        self.assertEqual(f_6.getvalue(), expected_output_6)

        rectangle_instance_7 = Rectangle(5, 3, 5)
        f_7 = io.StringIO()
        with redirect_stdout(f_7):
            rectangle_instance_7.display()
        expected_output_7 = """\
     #####
     #####
     #####
"""
        self.assertEqual(f_7.getvalue(), expected_output_7)

        rectangle_instance_8 = Rectangle(5, 3, 0, 4)
        f_8 = io.StringIO()
        with redirect_stdout(f_8):
            rectangle_instance_8.display()
        expected_output_8 = """\




#####
#####
#####
"""
        self.assertEqual(f_8.getvalue(), expected_output_8)

    # ----------------- Task 6 ------------------------
    def test_str_with_no_args(self):
        """
        Tests the __str__() method signature when called without any arguments

        Ensures that calling the __str__() method without any arguments
        raises a TypeError with a specific error message.
        """
        rectangle_instance = Rectangle(5, 2)
        with self.assertRaises(TypeError) as error_context:
            Rectangle.__str__()
        error_msg = "__str__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(error_context.exception), error_msg)

    def test_str(self):
        """
        Tests the __str__() method return value
        for different rectangle configurations.

        This test verifies the correctness of the __str__() method
        by comparing its return value against expected string representations
        for various rectangle dimensions, positions, and IDs.
        """
        # Test case 1
        rectangle_instance_1 = Rectangle(5, 2)
        expected_output_1 = '[Rectangle] (1) 0/0 - 5/2'
        self.assertEqual(str(rectangle_instance_1), expected_output_1)

        # Test case 2
        rectangle_instance_2 = Rectangle(1, 1, 1)
        expected_output_2 = '[Rectangle] (2) 1/0 - 1/1'
        self.assertEqual(str(rectangle_instance_2), expected_output_2)

        # Test case 3
        rectangle_instance_3 = Rectangle(3, 4, 5, 6)
        expected_output_3 = '[Rectangle] (3) 5/6 - 3/4'
        self.assertEqual(str(rectangle_instance_3), expected_output_3)

        # Additional test cases
        Base._Base__nb_objects = 0
        rectangle_instance_4 = Rectangle(4, 6, 2, 1, 12)
        expected_output_4 = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(str(rectangle_instance_4), expected_output_4)

        rectangle_instance_5 = Rectangle(5, 5, 1)
        expected_output_5 = "[Rectangle] (1) 1/0 - 5/5"
        self.assertEqual(str(rectangle_instance_5), expected_output_5)

    # ----------------- Task 8 and 9 ------------------------
    def test_update_with_no_args(self):
        """
        Tests the update() method signature when called without any arguments

        Ensures that calling the update() method without any arguments
        raises a TypeError with a specific error message.
        Verifies that the rectangle instance remains unchanged after update()
        """
        rectangle_instance = Rectangle(5, 2)
        with self.assertRaises(TypeError) as error_context:
            Rectangle.update()
        error_message = "update() missing 1 required positional argument: \
                'self'"
        self.assertEqual(str(error_context.exception), error_message)

        original_state = rectangle_instance.__dict__.copy()
        rectangle_instance.update()
        self.assertEqual(rectangle_instance.__dict__, original_state)

    def test_update_with_args(self):
        """
        Tests the update() method with positional arguments.

        Checks the behavior of the update() method when provided with
        different numbers of positional arguments. It verifies that the
        attributes of the rectangle instance are updated accordingly
        and that the update() method handles invalid values by raising
        ValueError.
        """
        rectangle_instance = Rectangle(5, 2)
        original_state = rectangle_instance.__dict__.copy()

        # Update with ID only
        rectangle_instance.update(10)
        original_state["id"] = 10
        self.assertEqual(rectangle_instance.__dict__, original_state)

        # Update with ID and width
        rectangle_instance.update(10, 5)
        original_state["_Rectangle__width"] = 5
        self.assertEqual(rectangle_instance.__dict__, original_state)

        # Update with ID, width, and height
        rectangle_instance.update(10, 5, 17)
        original_state["_Rectangle__height"] = 17
        self.assertEqual(rectangle_instance.__dict__, original_state)

        # Update with ID, width, height, and x
        rectangle_instance.update(10, 5, 17, 20)
        original_state["_Rectangle__x"] = 20
        self.assertEqual(rectangle_instance.__dict__, original_state)

        # Update with ID, width, height, x, and y
        rectangle_instance.update(10, 5, 17, 20, 25)
        original_state["_Rectangle__y"] = 25
        self.assertEqual(rectangle_instance.__dict__, original_state)

    def test_update_invalid_args(self):
        """
        Tests the update() method with invalid positional arguments.

        Checks the behavior of the update() method when provided with
        invalid positional arguments.
        It verifies that the update() method raises the appropriate ValueError
        for different scenarios:
        - Negative width value.
        - Negative height value.
        - Negative x value.
        - Negative y value.
        Ensures that the rectangle instance is unchanged after each update()
        """
        rectangle_instance = Rectangle(5, 2)
        original_state = rectangle_instance.__dict__.copy()

        # Update with ID only
        rectangle_instance.update(10)
        original_state["id"] = 10
        self.assertEqual(rectangle_instance.__dict__, original_state)

        # Attempt to update with negative width
        with self.assertRaises(ValueError) as error_context:
            rectangle_instance.update(10, -5)
        error_message = "width must be > 0"
        self.assertEqual(str(error_context.exception), error_message)

        # Attempt to update with negative height
        with self.assertRaises(ValueError) as error_context:
            rectangle_instance.update(10, 5, -17)
        error_message = "height must be > 0"
        self.assertEqual(str(error_context.exception), error_message)

        # Attempt to update with negative x
        with self.assertRaises(ValueError) as error_context:
            rectangle_instance.update(10, 5, 17, -20)
        error_message = "x must be >= 0"
        self.assertEqual(str(error_context.exception), error_message)

        # Attempt to update with negative y
        with self.assertRaises(ValueError) as error_context:
            rectangle_instance.update(10, 5, 17, 20, -25)
        error_message = "y must be >= 0"
        self.assertEqual(str(error_context.exception), error_message)

    def test_update_with_kwargs(self):
        """
        Tests the update() method with keyword arguments.

        Checks the behavior of the update() method when provided with
        keyword arguments. It verifies that the attributes of the rectangle
        instance are updated accordingly, and it includes additional test
        cases with mixed positional and keyword arguments.
        """
        rectangle_instance = Rectangle(5, 2)
        original_state = rectangle_instance.__dict__.copy()

        # Update with ID using keyword
        rectangle_instance.update(id=10)
        original_state["id"] = 10
        self.assertEqual(rectangle_instance.__dict__, original_state)

        # Update with width using keyword
        rectangle_instance.update(width=5)
        original_state["_Rectangle__width"] = 5
        self.assertEqual(rectangle_instance.__dict__, original_state)

        # Update with height using keyword
        rectangle_instance.update(height=17)
        original_state["_Rectangle__height"] = 17
        self.assertEqual(rectangle_instance.__dict__, original_state)

        # Update with x using keyword
        rectangle_instance.update(x=20)
        original_state["_Rectangle__x"] = 20
        self.assertEqual(rectangle_instance.__dict__, original_state)

        # Update with y using keyword
        rectangle_instance.update(y=25)
        original_state["_Rectangle__y"] = 25
        self.assertEqual(rectangle_instance.__dict__, original_state)

        # Additional test cases with mixed keyword arguments
        rectangle_instance.update(y=25, id=10, height=17, x=20, width=5)
        self.assertEqual(rectangle_instance.__dict__, original_state)

    def test_update_more_kwargs(self):
        """
        Tests the update() method with keyword arguments.

        It verifies that the update() method correctly updates
        the attributes of the rectangle instance based on the provided kwargs
        It also tests the interaction with the 'id' attribute.
        """
        rectangle_instance = Rectangle(5, 2)
        original_state = rectangle_instance.__dict__.copy()

        # Update with ID only
        rectangle_instance.update(id=10)
        original_state["id"] = 10
        self.assertEqual(rectangle_instance.__dict__, original_state)

        # Update with ID and width
        rectangle_instance.update(id=10, width=5)
        original_state["_Rectangle__width"] = 5
        self.assertEqual(rectangle_instance.__dict__, original_state)

        # Update with ID, width, and height
        rectangle_instance.update(id=10, width=5, height=17)
        original_state["_Rectangle__height"] = 17
        self.assertEqual(rectangle_instance.__dict__, original_state)

        # Update with ID, width, height, x
        rectangle_instance.update(id=10, width=5, height=17, x=20)
        original_state["_Rectangle__x"] = 20
        self.assertEqual(rectangle_instance.__dict__, original_state)

        # Update with ID, width, height, x, and y
        rectangle_instance.update(id=10, width=5, height=17, x=20, y=25)
        original_state["_Rectangle__y"] = 25
        self.assertEqual(rectangle_instance.__dict__, original_state)

        # Update with y, id, height, x, and width (order changed)
        rectangle_instance.update(y=25, id=10, height=17, x=20, width=5)
        self.assertEqual(rectangle_instance.__dict__, original_state)

        # Test updating a rectangle instance with a specific 'id' value
        Base._Base__nb_objects = 0
        rectangle_with_id = Rectangle(10, 10, 10, 10, id=1)
        self.assertEqual(str(rectangle_with_id),
                         "[Rectangle] (1) 10/10 - 10/10")

        # Update height attribute
        rectangle_with_id.update(height=1)
        self.assertEqual(str(rectangle_with_id),
                         "[Rectangle] (1) 10/10 - 10/1")

        # Update width and x attributes
        rectangle_with_id.update(width=1, x=2)
        self.assertEqual(str(rectangle_with_id), "[Rectangle] (1) 2/10 - 1/1")

        # Update y, width, x, and id attributes
        rectangle_with_id.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(rectangle_with_id), "[Rectangle] (89) 3/1 - 2/1")

        # Update x, height, y, and width attributes
        rectangle_with_id.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(rectangle_with_id), "[Rectangle] (89) 1/3 - 4/2")

        Base._Base__nb_objects = 0
        rectangle_instance = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(rectangle_instance),
                         "[Rectangle] (1) 10/10 - 10/10")

        # Update 'id' only
        rectangle_instance.update(id=89)
        self.assertEqual(str(rectangle_instance),
                         "[Rectangle] (89) 10/10 - 10/10")

        # Update 'id' and 'width'
        rectangle_instance.update(id=89, width=2)
        self.assertEqual(str(rectangle_instance),
                         "[Rectangle] (89) 10/10 - 2/10")

        # Update 'id', 'width', and 'height'
        rectangle_instance.update(id=89, width=2, height=3)
        self.assertEqual(str(rectangle_instance),
                         "[Rectangle] (89) 10/10 - 2/3")

        # Update 'id', 'width', 'height', 'x', and 'y'
        rectangle_instance.update(id=89, width=2, height=3, x=4, y=5)
        self.assertEqual(str(rectangle_instance),
                         "[Rectangle] (89) 4/5 - 2/3")

    # ----------------- Task 13 ------------------------
    def test_to_dictionary_method_func(self):
        """
        Tests the to_dictionary() method signature and functionality.

        Covers the to_dictionary() method of the Rectangle class.
        It checks the method's signature, validates if the returned
        dictionary contains the correct values, and verifies the consistency
        between the original Rectangle instance and a new instance created
        using the update() method.
        """
        with self.assertRaises(TypeError) as error_context:
            # Check if the to_dictionary() method has the correct signature
            Rectangle.to_dictionary()
        error_msg = "to_dictionary() missing 1 required positional argument: \
'self'"
        self.assertEqual(str(error_context.exception), error_msg)

        # Test to_dictionary() with different instances
        rectangle_instance = Rectangle(1, 2)
        expected_dict = {'x': 0, 'y': 0, 'width': 1, 'id': 1, 'height': 2}
        self.assertEqual(rectangle_instance.to_dictionary(), expected_dict)

        rectangle_instance = Rectangle(1, 2, 3, 4, 5)
        expected_dict = {'x': 3, 'y': 4, 'width': 1, 'id': 5, 'height': 2}
        self.assertEqual(rectangle_instance.to_dictionary(), expected_dict)

        rectangle_instance.x = 10
        rectangle_instance.y = 20
        rectangle_instance.width = 30
        rectangle_instance.height = 40
        expected_dict = {'x': 10, 'y': 20, 'width': 30, 'id': 5, 'height': 40}
        self.assertEqual(rectangle_instance.to_dictionary(), expected_dict)

        # Check consistency between original and new instance using update()
        original_instance = Rectangle(10, 2, 1, 9)
        original_dict = original_instance.to_dictionary()
        new_instance = Rectangle(1, 1)
        new_instance.update(**original_dict)
        self.assertEqual(str(original_instance), str(new_instance))
        self.assertNotEqual(original_instance, new_instance)


if __name__ == "__main__":
    unittest.main()
