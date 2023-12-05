#!/usr/bin/python3
"""Module to write an empty class
"""

class BaseGeometry:
    """This is the base class for making geometric shapes"""
    def area(self):
        """Determines area of the object"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Checks if value is an integer"""

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
