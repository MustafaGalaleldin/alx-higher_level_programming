#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if j > i:
            print("{:d}{:d}".format(i, j), end="\n" if (i == 8 andj == 9) 
                    else ", ")
