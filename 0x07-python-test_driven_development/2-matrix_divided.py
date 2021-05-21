#!/usr/bin/python3

"""
Add module matrix divided

Divide all elements in the matrix (list of lists) by the second arg
"""

def matrix_divided(matrix, div):
    """
    Return a new matrix with the elements divided by div
    rounded by 2 decimal
    """
    row_Len = []

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    for row in matrix:
        row_Len.append(len(row))
        if len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")

        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
        
    lenTester = list(set(row_Len))
    if len(lenTester) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(x / div, 2) for x in row] for row in matrix]

    return new_matrix





                



        
