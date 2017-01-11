#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    for i in range(0, len(my_list)):
        if i == idx:
            my_list[idx] = element  # replace element at idx with a new_element
    return (my_list)
