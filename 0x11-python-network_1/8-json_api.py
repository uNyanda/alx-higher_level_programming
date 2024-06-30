#!/usr/bin/python3
"""
This script takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
import sys


def fetch_user():
    """
    Handles sending a POST request with a letter as a parameter
    from the command line and process the JSON response.
    """
    # Get letter from command-line arguments or set to empty string if no
    letter = sys.argv[1] if len(sys.argv) > 1 else ""

    # Prepare the data for the POST request
    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': letter}

    # Send the POST request
    response = requests.post(url, data=data)

    try:
        # Attempt to parse the JSON respons
        json_response = response.json()

        # Check if json_response is not empty
        if json_response:
            print(f"[{json_response.get('id')}] {json_response.get('name')}")
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')


if __name__ == '__main__':
    fetch_user()
