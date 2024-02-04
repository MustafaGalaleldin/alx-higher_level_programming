#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for i in range(len(matrix)):
        if not matrix[i]:
            print()
            continue
        for j in range(len(matrix[i])):
            print("{:d}".format(matrix[i][j]), end=" "
                           if j != len(matrix[i]) - 1 else "\n")
