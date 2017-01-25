#!/usr/bin/python3
"""
This is the Rectangle module.

This is a Rectangle class that defines a rectangle.
"""


class Rectangle:
    number_of_instances = 0

    """
    This is a rectangle class
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if int(width) < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if int(height) < 0:
            raise ValueError("height must be >= 0")
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if int(value) < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if int(value) < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        for i in range(self.__width):
            for j in range(self.__height):
                    string += "#"
            string += '\n'
        string = string[:-1]
        return (string)

    def __repr__(self):
        width = str(self.__width)
        height = str(self.__height)
        return ("Rectangle(" + width + ", " + height + ")")

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
