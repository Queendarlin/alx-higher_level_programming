#!/usr/bin/python3
"""
Module for a function that multiplies two matrices
"""


def matrix_mul(m_a, m_b):
    """
    Function to multiply two matrices.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Returns:
        list of lists: The result of the matrix multiplication.

    Raises:
        TypeError: If m_a or m_b is not a list, not a list of lists,
                   contains non-integer/float elements, or is not a rectangle.
        ValueError: If m_a or m_b is empty,
        or if the matrices can't be multiplied.
    """
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all((isinstance(item, int) or isinstance(item, float))
               for item in [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(item2, int) or isinstance(item2, float))
               for item2 in [num for row in m_b for num in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    changed_b = []
    for rb in range(len(m_b[0])):
        latest_row = []
        for cb in range(len(m_b)):
            latest_row.append(m_b[cb][rb])
        changed_b.append(latest_row)

    latest_matrix = []
    for row in m_a:
        latest_row = []
        for col in changed_b:
            product = 0
            for index in range(len(changed_b[0])):
                product += row[index] * col[index]
            latest_row.append(product)
        latest_matrix.append(latest_row)

    return latest_matrix


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/100-matrix_mul.txt")
