#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    a = my_list.copy()
    a.reverse()
    for i in a:
        print(i)
    del a
