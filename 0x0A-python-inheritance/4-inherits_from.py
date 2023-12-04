#!/usr/bin/python3

def inherits_from(obj, a_class):
    """This function checks if an object is an instance of a class
        or its subclass

        Args:
            obj: object to check inheritance
            a_class: class to check if obj is instance of

        Returns:
            True or False
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
