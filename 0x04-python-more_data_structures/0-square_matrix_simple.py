#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = matrix[:]
    new = [list(map(lambda y : y**2, x))for x in new]
    return new
