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
        '''setter'''
        self.validator('width', value, True)
        self.__width = value

    @property
    def height(self):
        '''Height of this rectangle.'''
        return self.__height

    @height.setter
    def height(self, value):
        '''setter'''
        self.validator('height', value, True)
        self.__height = value

    @property
    def x(self):
        '''x of this rectangle.'''
        return self.__x

    @x.setter
    def x(self, value):
        '''setter'''
        self.validator('x', value, False)
        self.__x = value

    @property
    def y(self):
        '''y of this rectangle.'''
        return self.__y

    @y.setter
    def y(self, value):
        '''setter'''
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

    def update2(self, id=None, width=None, height=None, x=None, y=None):
        ''' updating process '''
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''Updates instance attributes via no-keyword & keyword args.'''
        # print(args, kwargs)
        if args:
            self.update2(*args)
        if kwargs:
            self.update2(**kwargs)

    def to_dictionary(self):
        ''' returns the dictionary representation of a Rectangle '''
        return {'y': self.y, 'x': self.x, 'id': self.id,
                'width': self.width, 'height': self.height}
