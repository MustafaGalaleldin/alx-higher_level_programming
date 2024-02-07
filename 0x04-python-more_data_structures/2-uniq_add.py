#!/usr/bin/python3
def uniq_add(my_list=[]):
    from functools import reduce
    if not my_list:
        return 0
    a = list(set(my_list))
    return reduce(lambda x, y: x + y, a)
