#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = len(sys.argv) - 1
    if count == 0:
        print("{:d} argument.".format(count))

    elif count == 1:
        print("{:d} argument:".format(count))

    else:
        print("{:d} arguments:".format(count))  # 2+ arguments:

    if count >= 1:
        for n in range(0, count):
            print("{:d}: {}".format(n + 1, sys.argv[n + 1]))  # arg#Asc, argInp
