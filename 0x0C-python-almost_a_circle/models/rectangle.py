#!/usr/bin/python3
""" rectangle class """
from base import Base


class Rectangle(Base):
    """
    the class Rectangle that inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ constructor """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ width getter decorator"""
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter decorator"""
        self.__width = value

    @property
    def height(self):
        """ heigth getter decorator"""
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter decorator""" 
        self.__height = value

    @property
    def x(self):
        """ x getter decorator"""
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter decorator"""
        self.__x = value

    @property
    def y(self):
        """ y getter decorator"""
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter decorator"""
        self.__y = value
