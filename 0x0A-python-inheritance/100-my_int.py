#!/usr/bin/python3
"""
Module for MyInt class
"""


class MyInt(int):
    """
        A class representing MyInt that inherits from int.
        """

    def __eq__(self, other):
        """
        Inverts the behavior of the == operator.

        Args:
            other: Value to compare.

        Returns:
            True if the values are not equal; otherwise, False.
        """
        return False

    def __ne__(self, other):
        """
        Inverts the behavior of the != operator.

        Args:
            other: Value to compare.

        Returns:
            True if the values are equal; otherwise, False.
        """
        return True
