#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    a = []
    for k, v in a_dictionary.items():
        if v == value:
            a.append(k)
    for i in a:
        del a_dictionary[i]

    return a_dictionary
