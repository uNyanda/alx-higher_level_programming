#!/usr/bin/python3
"""
This script takes in a URL and an email address, sends a POST request
to the passed URL with the email as a parameter, and displays the body of
the response.
"""
import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}  # Prepare the data for the POST request

    response = requests.post(url, data=data)  # send the POST request

    print(response.text)  # Print the body of the response
