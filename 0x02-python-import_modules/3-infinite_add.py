#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    size = len(sys.argv) - 1
    for num in range(0, size):
        sum = sum + int(sys.argv[num + 1])
    print("{:d}".format(sum))
