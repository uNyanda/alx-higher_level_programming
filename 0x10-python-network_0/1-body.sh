#!/bin/bash
# Send a GET request to the specified URL and display the body (if status code is 200)
curl -s -o /dev/null -w "%{http_code}" -L "$1" | grep -q 200 && curl -s "$1"
