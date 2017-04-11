#!/bin/bash
# displays body size of response
curl -Is "$1" | grep Content-Length | cut -d' ' -f2
