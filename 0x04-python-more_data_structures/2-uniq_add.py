#!/usr/bin/python3
def uniq_add(my_list=[]):
    for unique in my_list:
        unique = set(my_list)
        return(sum(unique))