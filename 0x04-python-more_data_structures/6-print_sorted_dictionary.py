#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    mylist = sorted(a_dictionary)
    mydict = {key : a_dictionary[key] for key in mylist}
    for k, v in mydict.items():
        print("{}: {}".format(k, v))
