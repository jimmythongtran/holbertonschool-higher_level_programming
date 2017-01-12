#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    return {i for i in set_1 and set_2 if i not in set_1 or set_2}
