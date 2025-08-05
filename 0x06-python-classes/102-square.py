#!/usr/bin/python3
"getters an setters"


class Square:
    '''
    class Square that defines a square
     have size method also we have getter and setter
     '''
    def __init__(self, __size=0):
        if not isinstance(__size, int):
            raise TypeError("size must be an integer")
        elif __size < 0:
            raise ValueError("size must be >= 0")
        self.__size = __size

    def size(self):
        return self.__size**2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, other):
        return self.size == other.size

    def __ne__(self, o):
        return self.size != o.size

    def __lt__(self, o):
        return self.size < o.size

    def __gt__(self, o):
        return self.size > o.size

    def __ge__(self, o):
        return self.size >= o.size

    def __le__(self, o):
        return self.size <= o.size
