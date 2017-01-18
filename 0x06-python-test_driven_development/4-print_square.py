#!/usr/bin/python3
"""
"""
def print_square(size):
    """
    """
    # size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
    # if size is a float and is less than 0, raise a TypeError exception with the message size must be an integer
    # if size is less than 0, raise a ValueError exception with the message size must be >= 0
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()

if __name__ == '__main__':
    doctest.testfile(4-print_square.txt)
