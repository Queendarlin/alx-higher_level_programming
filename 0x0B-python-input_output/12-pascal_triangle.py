#!/usr/bin/python3
"""
Module for pascal_triangle
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list of lists: Pascal's triangle up to the nth row.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for itr in range(1, n):
        row = [1]
        for itr2 in range(1, itr):
            row.append(triangle[itr - 1][itr2 - 1] + triangle[itr - 1][itr2])
        row.append(1)
        triangle.append(row)

    return triangle
