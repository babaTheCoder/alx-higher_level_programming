#!/usr/bin/python3

"""This module divides all elements of a matrix by a given number"""


def matrix_divided(matrix, div):
    """Division of elements in a matrix
    Args:
        matrix (list): a multilevel list of integers/floats
        div (int): integer to use as denominaor of division

    Returns:
        new matrix contaning quotients
    """

    warn = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(div, (int, float)):
        """Checks to make sure denominator is a valid integer or float"""
        raise TypeError("div must be a number")
    elif div == 0:
        """Checks to make sure denominator is not zero"""
        raise ZeroDivisionError("division by zero")

    for i in range(len(matrix)):
        """Making sure the length of all list in the matrix has equal lenght"""
        if len(matrix[i]) != len(matrix[i - 1]):
            raise TypeError("Each row of matrix must have the same size")

    for i in matrix:
        """Makes sure all elements in the matrix are integers or  decimals"""
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError(warn)
    rows = len(matrix)
    cols = len(matrix[0])
    new_matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(len(matrix)):
        """divide all elements in matrix and puts the result in new matrix"""
        for j in range(len(matrix[i])):
            new_matrix[i][j] = round((matrix[i][j]/div), 2)

    return new_matrix
