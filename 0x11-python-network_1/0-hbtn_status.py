#!/usr/bin/python3
"""
This script fetches the status from https://alx-intranet.hbtn.io/status
using the urllib package and displays the body of the response.
"""
import urllib.request


def fetch_status():
    """
    Fetches the status from the link
    and displays the body of the response.
    """
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        content = response.read()
        utf8_content = content.decode("utf-8")

    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")
    print(f"\t- utf8 content: {utf8_content}")


if __name__ == "__main__":
    fetch_status()
