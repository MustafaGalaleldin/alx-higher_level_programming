#!/usr/bin/python3
"square module with size with optional val"


class Square:
    "class Square that defines a square with size with optional val"
    def __init__(self, __size=0):
        if not isinstance(__size, int):
            raise TypeError("size must be an integer")
        elif __size < 0:
            raise ValueError("size must be >= 0")

        self.__size = __size
