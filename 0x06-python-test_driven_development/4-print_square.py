#!/usr/bin/python3
"""
This is the print_square function
that iterates through the length of a square
and prints # characters
"""


def print_square(size):
    """
    prints # characters
    """
    if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
    if (isinstance(size, float) and size > 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()

if __name__ == '__main__':
    doctest.testfile(4-print_square.txt)
