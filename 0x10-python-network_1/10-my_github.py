#!/usr/bin/python3
"""
this takes in github credentials (un and pw) and uses the
Github API to display ID
"""
import requests
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    r = requests.get("https://api.github.com/user", auth=(user, password))
    print(r.json().get("id"))
