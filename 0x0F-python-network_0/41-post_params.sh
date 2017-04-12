#!/bin/bash
# this takes in a URL, sends a POST request to passed URL, and displays response body
curl -sL -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
