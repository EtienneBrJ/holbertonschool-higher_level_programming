#!/usr/bin/python3
def uniq_add(my_list=[]):
    newlist = set(my_list)
    res = 0
    for i in newlist:
        res += i
    return res
