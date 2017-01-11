#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if 0 <= idx <= len(my_list):
        del my_list[idx]
    return my_list
#    for i in my_list[:]:
#        my_list.remove(i)
#    return (my_list)
