#!/usr/bin/python3
'task 1'


def write_file(filename="", text=""):
    'write in file'
    with open(filename, mode='w', encoding='UTF8') as f:
        return f.write(text)
