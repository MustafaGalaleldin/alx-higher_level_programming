#!/usr/bin/python3
""" matrix mul """


def matrix_mul(m_a, m_b):
    """
    a function that multiplies 2 matrices
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list ")

    if type(m_b) is not list:
        raise TypeError("m_b must be a list ")

    m_a_rows, m_a_col, m_b_rows, m_b_col = [0, 0, 0, 0]

    for lst in m_a:
        m_a_rows += 1
        if type(lst) is not list:
            raise TypeError("m_a must be a list of lists")
        for member in lst:
            m_a_col += 1
            if type(member) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
    m_a_col //= m_a_rows

    for lst in m_b:
        m_b_rows += 1
        if type(lst) is not list:
            raise TypeError("m_b must be a list of lists")
        for member in lst:
            m_b_col += 1
            if type(member) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")
    m_b_col //= m_b_rows
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")

    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    length_a = len(m_a[0])
    for lst in m_a:
        if len(lst) != length_a:
            raise TypeError("each row of m_a must be of the same size")

    length_b = len(m_b[0])
    for lst in m_b:
        if len(lst) != length_b:
            raise TypeError("each row of m_b must be of the same size")

    if m_a_col != m_b_rows:
        raise ValueError("m_a and m_b can't be multiplied")

    mult = []
    sublst = []
    val, mat_col = [0, 0]
    for mat_row in range(m_a_rows):
        for i in range(m_a_col):
            for j in range(m_b_col):
                val += m_a[mat_row][j] * m_b[j][mat_col]
            sublst.append(val)
            val = 0
            mat_col += 1
        mult.append(sublst)
        sublst = []
        mat_col = 0

    return mult
