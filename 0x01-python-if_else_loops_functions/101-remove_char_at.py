#!/usr/bin/python3
def remove_char_at(str, n):
    n_str = ''
    i = 0
    for c in str:
        if i != n:
            n_str += str[i]
        i += 1
    return n_str
