#!/usr/bin/python3
"""
this takes in a string and sends a search request to
the Star Wars API
"""
import requests
import sys


if __name__ == "__main__":
    url = "https://swapi.co/api/people/?search=" + sys.argv[1]
    r = requests.get(url)
    # print(r.text)
    count = r.json()["count"]
    search = r.json()["results"]
    print("Number of result: {}".format(count))
    for i in search:
        print(i["name"])
