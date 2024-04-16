#!/usr/bin/python3
'''
task 0
'''
def read_file(filename=""):
    'read a file'
    with open(filename) as f:
        print(f.read())
