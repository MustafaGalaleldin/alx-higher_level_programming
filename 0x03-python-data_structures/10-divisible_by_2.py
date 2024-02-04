#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    a = []
    for i in my_list:
        if not i % 2:
            a.append(True)
        else:
            a.append(False)

    return a
