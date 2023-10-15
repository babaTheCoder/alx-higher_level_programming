#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""This module defines a geometric shape"""


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        if integer_validator("width", width):
            self.__width = width
        if integer_validator("height", height):
            self.__height = height
