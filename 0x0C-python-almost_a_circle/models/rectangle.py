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
        self.validator('width', width, True)
        self.validator('height', height, True)
        self.validator('x', x, False)
        self.validator('y', y, False)
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
        self.validator('width', value, True)
        self.__width = value

    @property
    def height(self):
        '''Height of this rectangle.'''
        return self.__height

    @height.setter
    def height(self, value):
        self.validator('height', value, True)
        self.__height = value

    @property
    def x(self):
        '''x of this rectangle.'''
        return self.__x

    @x.setter
    def x(self, value):
        self.validator('x', value, False)
        self.__x = value

    @property
    def y(self):
        '''y of this rectangle.'''
        return self.__y

    @y.setter
    def y(self, value):
        self.validator('y', value, False)
        self.__y = value

    def validator(self, name, val, sizes=True):
        ''' validating method '''
        if type(val) is not int:
            raise TypeError(f"{name} must be an integer")
        if sizes and val <= 0:
            raise ValueError(f"{name} must be > 0")
        elif not sizes and val < 0:
            raise ValueError(f"{name} must be >= 0")

    def area(self):
        ''' return recangle area '''
        return self.width * self.height

    def display(self):
        """
        prints in stdout the Rectangle instance with the character #
        """
        for y in range(self.y):
            print()
        for i in range(self.height):
            for x in range(self.x):
                print(' ', end='')
            for j in range(self.width):
                print('#', end='\n' if j == self.width - 1 else '')

    def __str__(self):
        """ for printing """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y}"\
            f" - {self.width}/{self.height}"

    def update(self, *args):
        """
        assigns an argument to each attribute
        """
        for num, i in enumerate(args):
            if num == 0:
                self.id = i
            elif num == 1:
                self.width = i
            elif num == 2:
                self.height = i
            elif num == 3:
                self.x = i
            elif num == 4:
                self.y = i
