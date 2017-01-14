#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    i = 0
    while i < list_length:
        try:
            new_list.append(my_list_1[i] / my_list_2[i])
# [my_list_1i/my_list_2i for my_list1i,my_list2i in zip(my_list1,my_list2)]
        except TypeError:
            print("wrong type")
            new_list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        except IndexError:
            print("out of range")
            new_list.append(0)
        finally:
            i += 1
    return (new_list)  # with all divisions
