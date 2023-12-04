#!/usr/bin/python3

class BaseGeometry:
    """This is the base class for making geometric shapes"""
    def area(self):
        """Determines area of the object"""
        raise Exception("area() is not implemented")
