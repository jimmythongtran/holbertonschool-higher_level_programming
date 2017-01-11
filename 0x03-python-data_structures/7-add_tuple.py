#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # if user passes in an empty tuple, end up with an index out of range error
    tuple_a += (0, 0)
    tuple_b += (0, 0)
    return(tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
