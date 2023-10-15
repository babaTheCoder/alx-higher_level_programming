#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""This module defines a geometric shape"""


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        return self.__width * self.__height
