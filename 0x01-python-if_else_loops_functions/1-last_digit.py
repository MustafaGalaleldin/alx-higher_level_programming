#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    num = number % 10
else:
    num = number % -10
print(f"Last digit of {number:d} is {num:d} and is ", end="")
if num > 5:
    print("greater than 5")
elif num == 0:
    print("0")
elif num < 6 and num != 0:
    print("less than 6 and not 0")
