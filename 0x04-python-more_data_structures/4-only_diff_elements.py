#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    unique = []
    {unique.append(i) for i in set_1 if i not in set_2}
    {unique.append(i) for i in set_2 if i not in set_1}
#    return {i for i in set_1 and set_2 if i not in set_1 or set_2}
    return unique
