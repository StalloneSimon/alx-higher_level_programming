#!/usr/bin/python3
"""

A funcions that outputs "My name is <first name> <last name>"

"""


def say_my_name(first_name, last_name=""):
    """
    Simple code that prints "My name is <first name> <last name>"
    """
    if not (isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    if not (isinstance(last_name, str)):
        raise TypeError("last_name must be a string")
    try:
        print("My name is {:s} {:s}".format(first_name, last_name))
    except Exception as e:
        raise Exception(e)
