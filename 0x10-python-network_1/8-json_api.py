#!/usr/bin/python3
"""
this takes in a letter and sends in a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2 or not sys.argv[1].isalpha():
        print("No result")
    else:
        q = sys.argv[1]
        url = "http://0.0.0.0:5000/search_user"
        r = requests.post(url, data={'q': q})
        theId = r.json().get("id")
        name = r.json().get("name")
        print("[{}] {}".format(theId, name))
