#!/bin/bash
#sends a DELETE request to the URL passes as 1st arg, displays response body
curl -sL -X DELETE "$1"
