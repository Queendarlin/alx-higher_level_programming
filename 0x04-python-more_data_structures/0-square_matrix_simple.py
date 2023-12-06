#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = [[0 for _ in row] for row in matrix]

    for rows in range(len(matrix)):
        for columns in range(len(matrix[rows])):
            new_matrix[rows][columns] = matrix[rows][columns] ** 2

    return new_matrix
