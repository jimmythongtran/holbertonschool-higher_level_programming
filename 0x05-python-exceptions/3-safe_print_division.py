#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        i = (a / b)
    except (ZeroDivisionError, ValueError):
        i = None
    finally:
        print("{}{}".format("Inside result: ", i))
        return (i)
