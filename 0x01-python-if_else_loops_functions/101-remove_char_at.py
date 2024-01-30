#!/usr/bin/python3
def remove_char_at(str, n):
    mystr = str[:n] + str[n + 1:]
    return mystr
