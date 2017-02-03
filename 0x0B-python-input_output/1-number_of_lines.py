#!/usr/bin/python3
def number_of_lines(filename=""):
    with open(filename, encoding="UTF8") as f:
        count_line = 0
        for lines in f:
            count_line += 1
        return (count_line)
