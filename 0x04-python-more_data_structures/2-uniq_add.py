#!/usr/bin/python3
def uniq_add(my_list=[]):
    from functools import reduce
    a = list(set(my_list))
    return reduce(lambda x, y: x + y, a)
