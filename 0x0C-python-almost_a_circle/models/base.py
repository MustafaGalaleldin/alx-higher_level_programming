#!/usr/bin/python3
"""
base class
"""
import json


class Base:
    """ the base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
        returns the JSON string representation of list_dictionaries
        '''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        writes the JSON string representation of list_objs to a file
        '''
        from models.rectangle import Rectangle

        filename = cls.__name__ + '.json'

        with open(filename, 'w') as f:
            if list_objs is None or len(list_objs) == 0:
                f.write(cls.to_json_string([]))
            else:
                for i in list_objs:
                    f.write(cls.to_json_string(i.to_dictionary()))

    @staticmethod
    def from_json_string(json_string):
        '''returns the list of JSON string representation'''
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''returns an instance with all attributes already set'''
        from models.rectangle import Rectangle
        dummy = Rectangle(1, 1)
        dummy.update(**dictionary)
        return dummy

        '''def update2(self, id=None, width=None, height=None, x=None, y=None):
        """ updating process """
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y'''

    """def update(self, *args, **kwargs):
        '''Updates instance attributes via no-keyword & keyword args.'''
        # print(args, kwargs)
        if args:
            self.update2(*args)
        if kwargs:
            self.update2(**kwargs)"""
