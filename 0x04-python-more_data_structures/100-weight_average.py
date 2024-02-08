#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    summ = 0
    numm = 0
    for t in my_list:
        summ += t[0] * t[1]
        numm += t[1]
    return summ / numm
