#!/usr/bin/python3
""" 1st task """


class MyList(list):
    """ MyList """
    def print_sorted(self):
        new_list = self[:]
        new_list.sort()
        print(new_list)
