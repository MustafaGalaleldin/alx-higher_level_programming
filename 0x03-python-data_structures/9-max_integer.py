#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    ret = my_list[0]
    for i in my_list:
        if ret < i:
            ret = i
    return ret
