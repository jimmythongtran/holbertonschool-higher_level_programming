#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord('a') <= ord(i) <= ord('z'):
            var = (chr(ord(i) - 32))
        else:
            var = (i)
        print("{}".format(var), end="")
    print("{}".format(""))
