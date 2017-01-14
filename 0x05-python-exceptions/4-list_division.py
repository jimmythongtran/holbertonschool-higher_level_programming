#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    try:
        new_list = []
        for i in range(0, len(my_list1)):
            new_list.append(my_list1[i] / my_list2[i])
#        list_length = [my_list_1i/my_list_2i for my_list1i,my_list2i in zip(my_list1,my_list2)]
    except TypeError:
        print("wrong type")
    except ZeroDivisionError:
        print("division by 0")
    except IndexError:
        print("out of range")
    finally:
        return (new_list) # with all divisions
