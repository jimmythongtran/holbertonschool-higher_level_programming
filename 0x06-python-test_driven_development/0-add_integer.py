#!/usr/bin/python3

def add_integer(a, b):
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    return int(a + b)

if __name__ == '__main__':
    import doctest
    doctest.testfile(0-add_integer.txt)
