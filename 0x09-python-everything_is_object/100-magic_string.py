#!/usr/bin/python3
def magic_string():
    magic_string.calc = getattr(magic_string, 'calc', 0) + 1
    return ", ".join(["BestSchool" for i in range(magic_string.calc)])
