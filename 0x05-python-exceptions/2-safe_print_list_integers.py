#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    count = 0  # times an error hasn't been raised
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except TypeError:
            pass
        except ValueError:
            pass
        i += 1
    print("")
    return (count)
