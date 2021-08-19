#!/usr/bin/python3
# Finds a peak in a list of unsorted integers


def find_peak(list_of_integers):
    """ Return the int_max of the list if not NULL"""
    if len(list_of_integers) == 0:
        return None
    list_of_integers.sort()
    return list_of_integers[-1]
