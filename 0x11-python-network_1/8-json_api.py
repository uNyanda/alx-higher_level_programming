#!/usr/bin/python3
"""
This script takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
import sys


if __name__ == "__main__":
    # Get the letter from the command-line arguments or set to empty string if no
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    # Prepare the data for the POST request
    data = {'q': letter}

    # Send the POST request
    response = requests.post('http://0.0.0.0:5000/search_user', data=data)

    try:
        # Attempt to parse the JSON respons
        json_response = response.json()
        if json_response:
            print(f'[{json_response.get('id')}] {json_response.get('name')}]')
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
