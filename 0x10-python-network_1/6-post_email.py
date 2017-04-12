#!/usr/bin/python3
"""
this takes in a URL and email, sends a POST request to
passed URL with email as parameter, lastly displays
response body
"""
import requests
import sys


if __name__ == "__main__":
    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
