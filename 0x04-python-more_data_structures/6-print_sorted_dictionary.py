#!/usr/bin/python3
def print_sorted_dictionary(my_dict):
    for key, value in sorted(my_dict.items()):
            print("{}: {}".format(key, value))
#    [value for (key, value) in sorted(my_dict.items()]
#    for key, value in my_dict.items():
        #  sort by ascii value
#        new_dict = sorted(my_dict, key=lambda k: k['
#            print(key, value)
