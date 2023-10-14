#!/usr/bin/python3

"""This module sorts a given list"""


class MyList(list):
    """This class returns the elements of a list in a sorted order"""

    def custom_sort(lst):
        """This functions sorts a list"""

        n = len(lst)
        new_lst = lst[:]
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if new_lst[j] > new_lst[j + 1]:
                    new_lst[j], new_lst[j + 1] = new_lst[j + 1], new_lst[j]
        return new_lst

    def print_sorted(self):
        """Prints out a sorted list"""
        sort_list = MyList.custom_sort(self)
        print(sort_list)
