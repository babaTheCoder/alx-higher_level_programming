#!/usr/bin/python3

"""This module divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Divides all elements in a matrix by non-zero integer

    Args:
        matrix (list of lists): matrix to divide
        div (int): non-zero divisor

    Returns:
        a matrix of dividends
    """

    if not (isinstance(matrix, list) and all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    lenOfRowOne = len(matrix[0])
    for row in matrix:
        if len(row) != lenOfRowOne:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[None]*len(row) for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_matrix[i][j] = round(matrix[i][j] / div, 2)

    return new_matrix
