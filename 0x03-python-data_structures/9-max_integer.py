#!/usr/bin/python3
def max_integer(my_list=[]):
    imax = None
    if my_list:
        for i in my_list:
            if i > imax:
                imax = i
        return imax
    return None
