#!/usr/bin/python3
def no_c(my_string):
    #  removes all characters c and C from a string
    #  strings are immutable, unicode
    result = ""
    for i in my_string:
        if not (i == 'c' or i == 'C'):
            result += i
            # return my_string without these
    return (result)
