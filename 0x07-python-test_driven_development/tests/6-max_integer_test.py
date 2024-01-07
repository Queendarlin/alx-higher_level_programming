#!/usr/bin/python3
"""
Unit testing for max_integer(list=[])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    class to define unittest for max_integer(list=[])
    """
    def test_normal_int_list(self):
        """
        To test different forms of normal list representation of integers
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([2, 1, 4, 3]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """To test an empty list"""
        self.assertIsNone(max_integer([]), None)

    def test_negative_numbers(self):
        """To test lists of negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-2, -1, -4, -3]), -1)
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)

    def test_mixed_numbers(self):
        """
        To test mixture of lists of integer and float numbers
        and negative with positive numbers
        """
        self.assertEqual(max_integer([1, -2, -3, 4]), 4)
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)
        self.assertEqual(max_integer([1, 1.5, 4.5, 4]), 4.5)

    def test_float_numbers(self):
        """To test a list of float numbers"""
        self.assertEqual(max_integer([1.5, 2.3, 3.5, 4.5]), 4.5)

    def test_string_type(self):
        """To test lists of strings"""
        self.assertEqual(max_integer("hello"), 'o')
        self.assertEqual(max_integer(""), None)


if __name__ == "__main__":
    unittest.main()
