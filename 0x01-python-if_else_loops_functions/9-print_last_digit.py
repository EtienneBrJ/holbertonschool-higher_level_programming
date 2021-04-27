#!/usr/bin/python3
def print_last_digit(n):
    if n < 0:
        n = -n
    last_dig = n % 10
    print(last_dig, end='')
    return last_dig
