#!/usr/bin/python3
"""Create a matrix division function"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix

    matrix must be a list of lists of integers or floats

    Raises:
        TypeError: if matrix must be a matrix (list of lists) of integers/float
        TypeError: if Each row of the matrix must have the same size
        TypeError: if div must be a number
        ZeroDivisionError: if division by zero
    """
    if not (isinstance(matrix, list)
            and all(isinstance(row, list) for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if not all(isinstance(num, (int, float)) for num in row):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    lenght = len(matrix[0])
    if len(row) != lenght:
        raise TypeError(
            "Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new = [[round(num / div, 2) for num in row] for row in matrix]

    return new
