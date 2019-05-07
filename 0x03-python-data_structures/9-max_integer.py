#!/usr/bin/python3
def max_integer(my_list=[]):
    imax = 0
    for i in my_list:
        if i > imax:
            imax = i
    return imax
