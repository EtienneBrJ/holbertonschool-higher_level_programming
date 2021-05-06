#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newdict = {}
    for i in a_dictionary:
        newdict[i] = 2 * a_dictionary[i]
    return newdict
