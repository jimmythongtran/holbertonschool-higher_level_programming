#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("{:d} argument.".format(len(sys.argv) -1)) # > 0 argument.

    if len(sys.argv) == 2:
        print("{:d} argument:".format(len(sys.argv) -1)) # > 1 argument:

    if len(sys.argv) > 2:
        print("{:d} arguments:".format(len(sys.argv) -1)) # > 2+ arguments:
#end=""
#end="s"

#print(sys.argv[]))
