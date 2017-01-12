#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for i in range(0, len(my_list)):
        if i == search:
            my_list[search] = replace
        return (my_list)
