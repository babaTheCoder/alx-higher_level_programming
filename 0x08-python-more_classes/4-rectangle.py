#!/usr/bin/python3
"""This module defines a rectangle"""


class Rectangle:
    """This is a rectangle class
    It allows the user to create new rectangle objects with custom dimensions
    Attributes:
        width (int): the width of the rectangle
        height (int): the  height of the rectangle
    """

    def __init__(self, width=0, height=0):
        """Initialize the Rectangle class

        Args:
            width (int): The value of width
            height (int): The value of height
        """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Allows for access of the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Allows to set the value of the rectangle's width

        Args:
            value (int): This is the dimension entered by the user

        Raises:
            ValueError: If the entered digit is negative
            TypeError: If the entered data is not an integer or a float
        """

        if isinstance(value, (int, float)):
            if value < 0:
                raise ValueError("Width must be >= 0")
            else:
                self.__width = value
        else:
            raise TypeError("Width must be an integer")

    @property
    def height(self):
        """Allows to access the value of the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Allows to set a value for the height

        Args:
            value(int): The height entered by the user

        Raises:
            ValueError: if the input is a negative integer
            TypeError: if the input is not an integer or a float
        """

        if isinstance(value, (int, float)):
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """This method calculates the area of the rectangle"""

        return self.__height * self.__width

    def perimeter(self):
        """Calculates and returns the perimeter of a rectangle"""

        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Defines how *str* function behaves when called on this class"""

        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width] * self.__height)

    def __repr__(self):
        """Returns a string representation of the rectangle
        This can be used to create a new instance by using eval()
        """

        return f'Rectangle({self.width}, {self.height})'
