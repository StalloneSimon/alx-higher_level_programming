#!/usr/bin/python3
"""
    This is a simple module for adding itegers in python
"""


def add_integer(a, b=98):
    """ add two integers or flots """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return (a + b)
