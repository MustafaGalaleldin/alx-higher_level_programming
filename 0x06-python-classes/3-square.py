#!/usr/bin/python3
"square module with size with optional val and area method"


class Square:
    "class Square that defines a square and have area method"
    def __init__(self, __size=0):
        if not isinstance(__size, int):
            raise TypeError("size must be an integer")
        elif __size < 0:
            raise ValueError("size must be >= 0")
        self.__size = __size

    def area(self):
        return self.__size**2
