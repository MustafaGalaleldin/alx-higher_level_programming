#!/usr/bin/python3
"square position"


class Square:
    '''
    class Square that defines a square
     have area method also we have getter and setter
     and print size and have postion
     '''
    def __init__(self, __size=0, __position=(0, 0)):
        if not isinstance(__size, int):
            raise TypeError("size must be an integer")
        elif __size < 0:
            raise ValueError("size must be >= 0")
        self.__size = __size
        if not (
            isinstance(__position, tuple) and
            isinstance(__position[0], int) and
            isinstance(__position[1], int) and
            __position[1] >= 0 and __position[0] >= 0 and
            len(__position) == 2
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = __position

    def area(self):
        return self.__size**2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                x = self.__position[0]
                for j in range(self.__size):
                    while x:
                        print("_", end="")
                        x -= 1
                    print("#", end='\n' if j == self.__size - 1 else "")

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not (
            isinstance(__position, tuple) and
            isinstance(__position[0], int) and
            isinstance(__position[1], int) and
            __position[1] >= 0 and __position[0] >= 0 and
            len(__position) == 2
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
