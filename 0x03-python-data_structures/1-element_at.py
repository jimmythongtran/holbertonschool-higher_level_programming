#!/usr/bin/python3
def element_at(my_list, idx):
    # 0 excludes negatives
    for i in range(0, len(my_list)):
        if i == idx:
            return (my_list[idx])

# good for debugging
# print("{:d}".format(i))
