#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_copied = my_list.copy()
    if idx < 0 or idx > len(my_list) - 1:
        return list_copied
    list_copied[idx] = element
    return list_copied
