#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    ret = 0
    for su in argv[1:]:
        ret += int(su)
    print(ret)
