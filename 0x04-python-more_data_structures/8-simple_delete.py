#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if not key or not a_dictionary or not key in a_dictionary:
        return a_dictionary
    del (a_dictionary[key])
    return a_dictionary
