#!/usr/bin/python3
'''
rectangle class
'''
from models.base import Base


class Rectangle(Base):
    '''
    the class Rectangle that inherits from Base
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        ''' constructor '''
        self.validator('width', width, sizes=True)
        self.validator('height', height, sizes=True)
        self.validator('x', x, sizes=False)
        self.validator('y', y, sizes=False)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        '''Width of this rectangle.'''
        return self.__width

    @width.setter
    def width(self, value):
        self.validator('width', width, sizes=True)
        self.__width = value

    @property
    def height(self):
        '''Height of this rectangle.'''
        return self.__height

    @height.setter
    def height(self, value):
        self.validator('height', height, sizes=True)
        self.__height = value

    @property
    def x(self):
        '''x of this rectangle.'''
        return self.__x

    @x.setter
    def x(self, value):
        self.validator('x', x, sizes=False)
        self.__x = value

    @property
    def y(self):
        '''y of this rectangle.'''
        return self.__y

    @y.setter
    def y(self, value):
        self.validator('y', y, sizes=False)
        self.__y = value

    def validator(self, name, val, sizes=True):
        ''' validating method '''
        if type(val) is not int:
            raise TypeError(f"{name} must be an integer")
        if sizes and val <= 0:
            raise ValueError(f"{name} must be > 0")
        elif not sizes and val < 0:
            raise ValueError(f"{name} must be >= 0")
