#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    l = len(argv) - 1
    print("{:d} ".format(l), end="")
    if l == 0:
        print("arguments.")
    else:
        print("argument:" if l == 1 else "arguments:")
        for idx, ar in enumerate(argv[1:]):
            print("{:d}: {:s}".format(idx + 1, ar))
