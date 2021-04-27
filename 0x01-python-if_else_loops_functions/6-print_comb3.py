#!/usr/bin/python3
for first_dig in range(0, 9):
    for sec_dig in range(first_dig + 1, 10):
        if first_dig == 8:
            print("{}{}".format(first_dig, sec_dig))
        else:
            print("{}{}".format(first_dig, sec_dig), end=", ")
