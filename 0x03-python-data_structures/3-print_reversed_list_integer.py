#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    a = my_list.copy()
    a.reverse()
    for i in a:
        print(i)

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)
