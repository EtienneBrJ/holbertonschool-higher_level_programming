#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for ligne in matrix:
        for col in ligne:
            print("{:d}".format(col), end=" " if col != ligne[-1] else "")
        print()
