#!/usr/bin/python3


"""This module inherits from base is for creating rectangles"""


from models.base import Base


class Rectangle(Base):
    """This is a basic rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    # width getter
    @property
    def width(self):
        return self.__width

    # width setter
    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    # height getter
    @property
    def height(self):
        return self.__height

    # height setter
    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    # x getter
    @property
    def x(self):
        return self.__x

    # x setter
    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    # y getter
    @property
    def y(self):
        return self.__y

    # y setter
    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """This method returns area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints out the rectangle object with '#'"""
        rows = "#" * self.__width
        for i in range(self.__height):
            print(f"{rows}")

    def __str__(self):
        """Defines how an instance is displayed"""
        return "[Rectangle] ({}) {}/{} -  {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)
