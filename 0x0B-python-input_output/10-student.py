#!/usr/bin/python3

"""Defines a student"""


class Student:
    """A student class

    Attrbs:
        first_name (str): The first name of the student
        last_name (str): The last name of the student
        age (int): The age of the student

    Returns:
        a dictionary representation of the student
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Create a dictionary representation of Student instance"""
        if attrs is None:
            return self.__dict__
        return {at: getattr(self, at) for at in attrs if hasattr(self, at)}
