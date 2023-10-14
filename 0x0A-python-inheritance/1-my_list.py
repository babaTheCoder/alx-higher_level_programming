#!/usr/bin/python3

"""This module sorts a given list"""

class MyList(list):
    """This class returns the elements of a list in a sorted order"""
    def print_sorted(self):
        new_list = sorted(self)
        print(new_list)
