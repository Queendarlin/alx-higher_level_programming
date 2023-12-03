#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for int_num in row:
            print("{:d}".format(int_num), end=" ")
        print()
