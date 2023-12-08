#!/usr/bin/python3


"""This module inherits from base is for creating rectangles"""


from models.base import Base


class Rectangle(Base):
    """This is a basic rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    # width getter
    @property
    def width(self):
        return self.__width

    # width setter
    @width.setter
    def width(self, width):
        self.__width = width

    # height getter
    @property
    def height(self):
        return self.__height

    # height setter
    @height.setter
    def height(self, height):
        self.__height = height

    # x getter
    @property
    def x(self):
        return self.__x

    # x setter
    @x.setter
    def x(self, x):
        self.__x = x

    # y getter
    @property
    def y(self):
        return self.__y

    # width setter
    @y.setter
    def y(self, y):
        self.__y = y
