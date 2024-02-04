#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if not my_list:
        return None

    if idx < 0 or idx > len(my_list) - 1:
        return my_list

    for x, i in enumerate(my_list):
        if x == idx:
            my_list.remove(i)
    return my_list
