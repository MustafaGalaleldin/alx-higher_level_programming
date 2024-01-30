#!/usr/bin/python3
def uppercase(str):

    '''
    check if upper

    Parameters:
    str: to check

    Return:
    string in upper

   '''

    for c in str:
        if 'a' <= c <= 'z':
            mc = ord(c) - 32
        else:
            mc = ord(c)
        print("{:c}".format(mc), end="")
    print("")
