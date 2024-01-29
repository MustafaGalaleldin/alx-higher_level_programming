#!/usr/bin/python3
for i in range(0, 100):
    if (i / 10 < 1):
        print("0", end="")
    if i == 99:
        print("{:d}". format(i))
    else:
        print("{:d}".format(i), end=", ")
