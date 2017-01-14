#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [replace if element == search else element for element in my_list]
#    new_list = my_list[:]
#    for i in range(0, len(my_list)):
#        if new_list[i] == search:
#            new_list.pop(new_list[i])
#            new_list.insert(i, replace)
#    return (new_list)
