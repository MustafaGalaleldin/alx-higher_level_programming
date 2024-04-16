#!/usr/bin/python3
'task 2'


def write_file(filename="", text=""):
    'append in file'
    with open(filename, mode='a') as f:
        return f.write(text)
