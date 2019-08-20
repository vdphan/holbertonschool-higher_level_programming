#!/usr/bin/python3
""" a function that finds a peak in a list of unsorted integers"""


def peak_re(l, start, end):
    """recursive way"""
    if start == end:
        return l[start]
    mid = (start + end) // 2
    if l[mid] >= l[mid - 1] and l[mid] >= l[mid + 1]:
        return l[mid]
    if l[mid + 1] >= l[mid]:
        return peak_re(l, mid + 1, end)
    else:
        return peak_re(l, start, mid - 1)
# def find_peak(list_of_integers):
#    """finds a peak in a list of unsorted integers"""
#    if len(list_of_integers) == 0:
#        return None
#    m = len(list_of_integers)
#    haf = m // 2
#    l = list_of_integers[:]
#    for i in range(0, haf):
#        if i == 0 and l[i] >= l[i + 1]:
#            return l[i]
#        elif l[i] >= l[i + 1] and l[i] >= l[i - 1]:
#            return l[i]
#        elif i == haf - 1 and l[i] >= l[i + 1] and l[i] >= l[i - 1]:
#            return l[i]
#    for i in range(haf, m):
#        if i == haf and l[i] >= l[i + 1] and l[i] >= l[i - 1]:
#            return l[i]
#        elif l[i] >= l[i + 1] and l[i] >= l[i - 1]:
#            return l[i]
#        elif i == m - 1 and l[i] >= l[i - 1]:
#            return l[i]


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    if len(list_of_integers) == 0:
        return None
    return peak_re(list_of_integers, 0, len(list_of_integers) - 1)
