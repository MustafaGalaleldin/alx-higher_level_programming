#!/usr/bin/python3
'task 2'


def append_write(filename="", text=""):
    'append in file'
    with open(filename, mode='a') as f:
        return f.write(text)
