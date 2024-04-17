#!/usr/bin/python3
""" 10th task """


class Student:
    """ my class """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        try:
            for a in attrs:
                if a is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__

        dico = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                dico[key] = value
        return dico
