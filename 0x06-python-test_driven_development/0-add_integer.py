#!/usr/bin/python3
"""
This is the add_integer function
that takes in two variables and returns their sum
Note: value can only be integers, not float or otherwise
"""


def add_integer(a, b):
    """
    returns the sum of two integer variables
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(a + b)

if __name__ == '__main__':
    import doctest
    doctest.testfile(0-add_integer.txt)
