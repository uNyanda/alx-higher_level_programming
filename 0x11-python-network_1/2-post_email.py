#!/usr/bin/python3
"""
This script sends a POST request to a given URL with an email as a parameter
and displays the response body.
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]  # get url from commandline args
    email = sys.argv[2]  # get the email from commandline args

    data = urllib.parse.urlencode({"email": email}).encode("utf-8")

    # create a request and send it
    with urllib.request.urlopen(url, data) as response:
        content = response.read().decode("utf-8")

    print(content)
