#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if not i % 3 :
            print("Fizz", end="" if i == 100 else " ")
        elif not i % 5:
            print("Buzz", end="" if i == 100 else " ")
        elif not i % 15:
            print("FizzBuzz", end="" if i == 100 else " ")
        else:
             print(i, end="" if i == 100 else " ")
