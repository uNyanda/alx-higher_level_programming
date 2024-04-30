#!/usr/bin/python3
"""
This script fetches the status from https://alx-intranet.hbtn.io/status
"""
import urllib.request


def main():
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        content = response.read()
        utf8_content = content.decode("utf-8")

    print("Body response:")
    print(f"    - type: {type(content)}")
    print(f"    - content: {content}")
    print(f"    - utf8 content: {utf8_content}")


if __name__ == "__main__":
    main()
