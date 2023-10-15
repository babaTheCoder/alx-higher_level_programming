#!/usr/bin/python3
"""This creates an empty Base Geometry class"""


class BaseGeometry:
    """Creates functions for geometrical operations"""

    def area(self):
        """Calculates the area of a geometrical shape"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Checks whether a value is an integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than zero".format(name))
