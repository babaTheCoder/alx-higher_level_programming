#!/usr/bin/python3

"""This module defines a square"""


class Square:
    """Square: an empty class that defines square
       Nothing happens here
    """

    def __init__(self, size=0):
        """This initializes the class when an instance is first created

        Args:
            size (int): dimensions for the square
        """

        if isinstance(size, (int, float)):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    @property
    def size(self):
        """Getter method for private attribute self"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for getting user input for size"""
        self.__size = value

    def area(self):
        """Calculates the area of the square"""
        return self.__size ** 2
