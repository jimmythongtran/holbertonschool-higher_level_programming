#!/usr/bin/python3
"""
This is the text_indentation function
that iterates through a string
otherwise raising a TypeError exception
"""
def text_indentation(text):
    """
    prints a string of text
    """
    # text must be a string, otherwise raise a TypeError exception with the message text must be a string
    if not (isinstance(text, str)):
            raise TypeError("text must be a string")
    for i in text:
        if not (i == '.' or i == '?' or i == ":"):
            print("{:s}".format(i), end="")
        else:
            print("{:s}\n".format(i))

if __name__ == '__main__':
        doctest.testfile(5-text_indentation.txt)
