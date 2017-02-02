#!/usr/bin/python3
"""
This module contains one class
https://github.com/anne75 developed the test
run it with python3 -m doctest ./tests/1-my_list.txt
"""
class MyList(list):
    """
    Inherits from the list class
    Assumes all elements in list are ints
    """
    def print_sorted(self):
        print("{:d}".format(sorted(self)))
