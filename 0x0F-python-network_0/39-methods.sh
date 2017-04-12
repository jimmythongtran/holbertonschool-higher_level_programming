#!/bin/bash
# this takes in a URL and displays all HTTP methods the server will accept
curl -sl -i -X OPTIONS "$1" | grep "Allow" | awk -F": " '{print $2}'
