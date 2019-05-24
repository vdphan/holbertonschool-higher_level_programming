#!/usr/bin/python3
def matrix_divided(matrix, div):
    s = 'matrix must be a matrix (list of lists) of integers/floats'
    if type(matrix) != list:
        raise TypeError(s)
    if len(matrix) == 0:
        raise TypeError(s)
    if any(type(i) != list for i in matrix):
        raise TypeError(s)
    if any(not i for i in matrix):
        raise TypeError(s)
    for i in matrix:
        for j in i:
            if type(j) != int and type(j) != float:
                raise TypeError(s)
    a = len(matrix[0])
    for i in range(1, len(matrix)):
        if len(matrix[i]) != a:
            raise TypeError('Each row of the matrix must have the same size')
    if type(div) != int and type(div) != float:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    b = [[x / div for x in i] for i in matrix]
    return [[round(m, 2) for m in n] for n in b]
