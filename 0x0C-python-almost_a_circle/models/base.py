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
        if list_objs is not None:
            list_objs = [o.to_dictionary() for o in list_objs]
        with open(filename, 'w') as f:
            if list_objs is None or len(list_objs) == 0:
                f.write(cls.to_json_string([]))
            else:
                f.write(cls.to_json_string(list_objs))

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
        from models.square import Square
        if cls.__name__ == 'Square':
            dummy = Square(size=1, x=0, y=0, id=None)
        else:
            dummy = Rectangle(width=1, height=1, x=0, y=0, id=None)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        '''returns a list of instances'''
        filename = cls.__name__ + '.json'
        try:
            with open(filename, 'r') as f:
                my_list = cls.from_json_string(f.read())
                list2 = []
                for dic in my_list:
                    list2.append(cls.create(**dic))
                return list2
        except FileNotFoundError:
            return []
