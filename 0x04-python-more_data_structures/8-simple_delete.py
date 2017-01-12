#!/usr/bin/python3
def simple_delete(my_dict, key=""):
    if my_dict == {} or my_dict is None:
        return None
    for i in my_dict:
        if i == my_dict[key]:
            del my_dict[key]
    return my_dict
