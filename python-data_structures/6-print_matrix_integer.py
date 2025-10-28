#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    Print a matrix of integers, one row per line, values separated by spaces.
    """
    for row in matrix:
        print(" ".join("{:d}".format(num) for num in row))
