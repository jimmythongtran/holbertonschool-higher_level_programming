#!/usr/bin/python3
def multiply_by_2(my_dict):
    new_dict = dict(my_dict)
    for i in new_dict:
        new_dict[i] *= 2
        return (new_dict)
#    my_dict = new_dict
# multiply the values by 2
#    multiplied = new_dict, key=new_dict.get * 2
#    return (multiplied)
