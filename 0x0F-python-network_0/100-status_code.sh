#!/bin/bash
# sends a request to URL passes as arg, displays status code of response
curl -s -o /dev/null -I -w "%{http_code}" "$1"
