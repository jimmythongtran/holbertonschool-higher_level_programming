#!/usr/bin/python3

def add(a, b):
    """Return the sum of a and b.
    >>> add(1, 2)
    3
    >>> add(100, -2)
    98
    >>> add(100.3, -2)
    98
    """
    return (int(a + b))

if __name__ == '__main__':
    from doctest
    doctest.testmod()
