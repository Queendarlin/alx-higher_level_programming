#!/usr/bin/python3
"""
Module for a function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Function to divide all elements of a matrix by a given number.

    Args:
        matrix (float or int): A list of lists containing integers or floats.
        div (float or int): The divisor of each element.

    Return: A new matrix with elements rounded to 2 decimal places.

    Raises:
         TypeError: If the matrix is not a list of lists of integers/floats,
                   if each row of the matrix does not have the same size,
                   or if div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")

    for matrix_row in matrix:
        if not isinstance(matrix_row, list) or len(matrix_row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")

        if len(matrix_row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        for row_elem in matrix_row:
            if not isinstance(row_elem, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
    return [[round(row_elem / div, 2) for row_elem in matrix_row]
            for matrix_row in matrix]
