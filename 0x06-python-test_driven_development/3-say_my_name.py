#!/usr/bin/python3
"""
This is the say_my_name function
that takes in two string variables and returns
the full string "My name is first_name last_name"
"""


def say_my_name(first_name, last_name=""):
    """
    returns the full string "My name is first_name last_name
    """
    if not (isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    if not (isinstance(last_name, str)):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))

if __name__ == '__main__':
    import doctest
    doctest.testfile(3-say_my_name.txt)
