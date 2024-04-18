#!/usr/bin/python3
""" 4th task """


def inherits_from(obj, a_class):
    """ def inherits_from """
    return isinstance(obj, a_class) and type(obj) != a_class
