#!/usr/bin/python3
a = 10
b = 5
from calculator_1 import add, sub, mul, div
print("{:d} + {:d} = {:d}".format(a, b, a + b))
print("{:d} - {:d} = {:d}".format(a, b, a - b))
print("{:d} * {:d} = {:d}".format(a, b, a * b))
print("{:d} / {:d} = {:.0f}".format(a, b, a / b))
