#!/usr/bin/python3
def no_c(my_string):
    a = ""
    for x, i in enumerate(my_string):
        if i != 'c' and i != 'C':
            a += i
    return a
