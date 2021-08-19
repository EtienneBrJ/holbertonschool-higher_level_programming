#!/usr/bin/python3
"""Find a peak"""


def find_peak(list_of_integers):
    """ Return the int_max of the list if not NULL"""
    if len(list_of_integers) == 0:
        return None
    return max(list_of_integers)
