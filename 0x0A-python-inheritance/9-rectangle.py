#!/usr/bin/python3
"""Module to write an empty class
"""


class BaseGeometry:
    """Geometry class
    """
    def area(self, width, height):
        """check area"""
        

    def integer_validator(self, name, value):
        """validates value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """inherits from BaseGeometry
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

        BaseGeometry.integer_validator(self, "width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)

    def area(self):
        """Calculates area of the Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
