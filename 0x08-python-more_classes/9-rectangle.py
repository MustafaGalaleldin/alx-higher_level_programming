#!/usr/bin/python3
'9th module'


class Rectangle:
    '''
    comparing two rectangles
    rec with getters and setters and some methods
    print rectangle
    repr
    del
    class attr
    '''
    print_symbol = '#'
    number_of_instances = 0

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
        Rectangle.number_of_instances += 1

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
                    ret += str(self.print_symbol)
                    if j == self. __width - 1:
                        if i != self.__height - 1:
                            ret += '\n'
            return ret

    def __repr__(self):
        return "Rectangle" + '(' + str(self.__width) \
             + ', ' + str(self.__height) + ')'

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if not (self.__height and self.__width):
            return 0
        else:
            return 2 * self.__height + 2 * self.__width

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        a = rect_1.area()
        b = rect_2.area()
        if a == b or a > b:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
