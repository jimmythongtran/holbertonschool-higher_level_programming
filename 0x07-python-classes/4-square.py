#!/usr/bin/python3
"""
This is the square module

This is a Square class that calculates area based on size
"""


class Square:
    """
    This is a square class
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not (isinstance(value, int)):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.size = value

    def area(self):
        return (self.size * self.size)
