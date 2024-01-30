#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    if not i % 2:
        print("{:c}".format(i), end="")
    else:
        print("{:c}".format(i - 32), end="")
