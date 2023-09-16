#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_diction = {}
    for key, val in a_dictionary.items():
        new_diction[key] = val * 2
    return new_diction
