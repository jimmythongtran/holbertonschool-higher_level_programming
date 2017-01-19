#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    for unique in my_list:
        if unique not in new_list:
            new_list.append(unique)
    return(sum(new_list))
#    for unique in my_list:
#        if my_list is None:
#            return None
#        unique = set(my_list)
#        return(sum(unique))
