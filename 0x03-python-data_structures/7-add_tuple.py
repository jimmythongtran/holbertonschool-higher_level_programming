#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    #  first element the addition of the first element of each argument
    a = tuple_a(0) + tuple_b(0)
    #  second element the addition of the second element of each argument
    b = tuple_a(1) + tuple_b(1)
#    if a or b > 2, use the value 0 for each missing integer
#    if a or b < 2, use only the first two integers
    return tuple(a, b)
