#!/usr/bin/python3
"""prints lists inherited
"""

class MyList(list):
    """child class of list
    """
    def print_sorted(self):
        """
        Module to sort a list
        """
        print(sorted(self.copy()))
