#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a += (0, 0)
    tuple_b += (0, 0)

    s1 = tuple_a[0] + tuple_b[0]
    s2 = tuple_a[1] + tuple_b[1]

    s = (s1, s2)
    return s
