#!/usr/bin/python3
''' square module '''
from models.rectangle import Rectangle


class Square(Rectangle):
    ''' class '''
    def __init__(self, size, x=0, y=0, id=None):
        ''' constructor '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        ''' to print '''
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        '''Size of this square.'''
        return self.width

    @size.setter
    def size(self, value):
        self.validator('width', value, True)
        self.validator('height', value, True)
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        '''Internal method that updates instance attributes via */**args.'''
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''Updates instance attributes via no-keyword & keyword args.'''
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        ''' returns the dictionary representation of a Square '''
        return {'y': self.y, 'x': self.x, 'id': self.id,
                'size': self.size}

    def to_csv(self):
        ''' square to csv'''
        return f"{self.id},{self.size},"\
            "{self.x},{self.y}"
