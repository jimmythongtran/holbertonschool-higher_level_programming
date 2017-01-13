#!/usr/bin/python3
def search_replace(my_list, search, replace):
    #  makes copy
    new_list = my_list[:]
    for i in range(0, len(my_list)):
        if new_list[i] == search:
            new_list.pop(new_list[i])
            new_list.insert(i, replace)
    return (new_list)
#        if i == search:
#            my_list[search] = replace
#        return (my_list)
