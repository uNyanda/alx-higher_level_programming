#!/usr/bin/python3
"""
This script fetches a URL, sends a request, and displays the value of the
X-Request-Id header.
"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]  # get url from command line
    with urllib.request.urlopen(url) as response:
        headers = response.info()
        x_request_id = headers.get("X-Request-Id")
        print(x_request_id)
