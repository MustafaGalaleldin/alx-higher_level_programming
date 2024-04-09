#!/usr/bin/python3
'fifth module'


class Rectangle:
    '''
    rec with getters and setters and some methods
    print rectangle
    repr
    '''
    def __init__(self, __width=0, __height=0):
        if not isinstance(__width, int):
            raise TypeError("width must be an integer")
        if __width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(__height, int):
            raise TypeError("height must be an integer")
        if __height < 0:
            raise ValueError("height must be >= 0")
        self.__width = __width
        self.__height = __height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __str__(self):
        if not (self.__height and self.__width):
            return ''
        else:
            ret = ""
            for i in range(self.__height):
                for j in range(self.__width):
                    ret += '#'
                    if j == self. __width - 1:
                        if i != self.__height - 1:
                            ret += '\n'
            return ret

    def __repr__(self):
        return "Rectangle" + '(' + str(self.__width) \
             + ', ' + str(self.__height) + ')'

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if not (self.__height and self.__width):
            return 0
        else:
            return 2 * self.__height + 2 * self.__width
