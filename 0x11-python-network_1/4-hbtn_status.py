#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status
"""
import requests


if __name__ == "__main__":
    response = requests.get('https://alx-intranet.hbtn.io/status')
    content = response.text
    content_type = type(content)

    print("Body response:")
    print(f'\t- type: {content_type}')
    print(f'\t- content: {content}')
