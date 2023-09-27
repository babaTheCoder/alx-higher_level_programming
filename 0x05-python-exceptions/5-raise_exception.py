#!/usr/bin/python3

def  raise_exception():
    try:
        print(12/'hello')
    except TypeError:
        raise TypeError
