#!/usr/bin/python3
""" matrix module """


def matrix_divided(matrix, div):
    """
    matrix
    """
    for lst in matrix:
        if type(lst) is not list:
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")

        for mem in lst:
            if type(mem) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")

    tall = len(matrix[0])
    for lst in matrix:
        if len(lst) != tall:
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise ValueError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    my_martix = []
    for lst in matrix:
        lst1 = []
        for mem in lst:
            lst1.append(round(mem / div, 2))
        my_martix.append(lst1)

    return my_martix
