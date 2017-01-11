#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list == None:
        return None
    for i in reversed(my_list):
        #  my_list.reverse()
        print("{:d}".format(i))
#  TODO: You have to handle the list when it == None
