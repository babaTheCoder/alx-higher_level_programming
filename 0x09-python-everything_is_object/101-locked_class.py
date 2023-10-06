#!/usr/bin/python3

class LockedClass:
    __slots__ = ['first_name']

    def __setattr__(self, name, value):
        if name != "first_name":
            raise AttributeError(f"Cannot create a new instance attribute '{name}'")
        self.__dict__(name) = value