#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(100.3, -2))
try:
    print(add_integer(4, "School"))
    print(add_integer("Holberton", 4))
    print(add_integer("Holberton", "School"))
    print(add_integer([1, 2, 3], 2))
    print(add_integer(2, [1, 2, 3]))
    print(add_integer({1: "yo"}, 1))
except Exception as e:
    print(e)
