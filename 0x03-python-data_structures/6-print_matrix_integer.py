#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return "\n"
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            print("{:d}".format(matrix[i][j]), end="")
            if j < len(matrix[i]) - 1:
                print(" ", end="")
        print ()
