#!/usr/bin/python3

import sys
#import getopt

# remove sys?

if len(sys.argv) == 1:
    print ("{:d} argument.".format(len(sys.argv) -1)) # > 0 argument:

if len(sys.argv) > 1:
    print ("{:d} arguments:".format(len(sys.argv))) # > 2+ arguments:

#print (getopt(sys.argv[1:]))
