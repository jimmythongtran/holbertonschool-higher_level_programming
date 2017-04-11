#!/usr/bin/python3
"""
this script takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of response
"""
import urllib.request
import sys

if __name__ == "__main__":

    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.info()
        print("{}".format(html.get('X-Request-Id')))
