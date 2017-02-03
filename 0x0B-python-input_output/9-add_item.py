#!/usr/bin/python3
import json
from sys import argv
import os.path

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
# saving list as JSON representation
filename = "add_item.json"
# check if file exists
if os.path.isfile(filename):
    myList = load_from_json_file(filename)
# if file doesn't exist, create it
else:
    myList = []
count = 0
# loop through argv not counting first arg
for i in argv:
    if count != 0:
        myList.append(i)
    count += 1
save_to_json_file(myList, filename)
