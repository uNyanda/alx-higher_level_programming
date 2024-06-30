#!/usr/bin/python3
"""
This script takes GitHub username and personal access token as arguments
and uses the GitHub API to display the user's ID.
"""
import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <username> <token>")
        sys.exit(1)

    username = sys.argv[1]
    token = sys.argv[2]

    url = f'https://api.github.com/users/{username}'
    headers = {
        "Authorization": f'token {token}',
        "Accept": "application/vnd.github.v3+json"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            user_data = response.json()
            print(user_data.get('id'))
        else:
            print(None)
    except requests.RequestException as e:
        print(f'Request failed: {e}')
        sys.exit(1)
