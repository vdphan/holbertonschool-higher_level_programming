#!/usr/bin/python3
""" a function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    if len(list_of_integers) == 0:
        return None
    m = len(list_of_integers)
    haf = m // 2
    l = list_of_integers[:]
    for i in range(0, haf):
        if i == 0 and l[i] >= l[i + 1]:
            return l[i]
        elif l[i] >= l[i + 1] and l[i] >= l[i - 1]:
            return l[i]
        elif i == haf - 1 and l[i] >= l[i + 1] and l[i] >= l[i - 1]:
            return l[i]
    for i in range(haf, m):
        if i == haf and l[i] >= l[i + 1] and l[i] >= l[i - 1]:
            return l[i]
        elif l[i] >= l[i + 1] and l[i] >= l[i - 1]:
            return l[i]
        elif i == m - 1 and l[i] >= l[i - 1]:
            return l[i]
