#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    try:
        list_length = [my_list_1i/my_list_2i for my_list1i,my_list2i in zip(my_list1,my_list2)]
    except TypeError:
        print("wrong type")
    except ZeroDivisionError:
        print("division by 0")
    except IndexError:
        print("out of range")
    finally:
        return (list_length) # with all divisions
