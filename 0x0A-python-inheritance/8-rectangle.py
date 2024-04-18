#!/usr/bin/python3
""" 8th task """
BaseGeometry = __import__('7-base_geometery').BaseGeometry


class Rectangle(BaseGeometry):
    """ BaseGeometry """
    def __init__(self, width, height):
        'init'
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
