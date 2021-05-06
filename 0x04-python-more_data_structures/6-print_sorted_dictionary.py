#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    newlist = sorted(a_dictionary)
    for i in newlist:
        print("{}: {}".format(i, a_dictionary[i]))
