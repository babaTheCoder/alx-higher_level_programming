#!/usr/bin/python3

"""This module defines a rectangle class"""


class Rectangle:
    """Class with width and height attribs"""

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """calculates perimeter of the circle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """Defines a string"""

        if self.__width == 0 or self.__height == 0:
            return ("")
        row = "#" * self.__width

        return f'{row}\n' * self.__height

    def __repr__(self):
        """returns string that can be passed to eval"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """runs when an instance is deleted"""
        print("Bye rectangle...")
