#!/usr/bin/python3
"""
this takes in a URL and email, sends a POST request to
passed URL with email as parameter, lastly displays
response body
"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    try:
        print(r.text)
    except Exception as e:
        print("Error code: {}".format(r.status_code))
