#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        tmp = my_list[0]
        for i in range(len(my_list)):
            if my_list[i] > tmp:
                tmp = my_list[i]
        return tmp
    else:
        return None
