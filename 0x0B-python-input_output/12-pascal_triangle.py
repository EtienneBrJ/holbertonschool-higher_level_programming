#!/usr/bin/python3
""" Module pascale triangle.
"""


def pascal_triangle(n):
    """ Return a list of a list
        representing the Pascal's triangle of n.
    """
    pascalTriangle = []

    for row in range(1, n+1):
        intList = []
        for col in range(row):
            if col == 0 or col == row - 1:
                intList.append(1)
            else:
                n = pascalTriangle[row-2][col-1] + pascalTriangle[row-2][col]
                pascalTriangle.append(n)
        pascalTriangle.append(intList)

    return pascalTriangle
