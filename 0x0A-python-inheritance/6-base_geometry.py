#!/usr/bin/python3
"""Module to write an empty class
"""

class BaseGeometry:
    """This is the base class for making geometric shapes"""
    def area(self):
        """Determines area of the object"""
        raise Exception("area() is not implemented")
