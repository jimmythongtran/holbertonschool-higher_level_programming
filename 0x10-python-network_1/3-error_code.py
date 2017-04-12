#!/usr/bin/python3
"""
this takes in a URL, sends a request to URL, displays
response body (decoded in utf-8)
"""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))

    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
