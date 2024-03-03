#!/usr/bin/python3
""" get status"""


if __name__ == "__main__":
    import requests
    import sys

    try:
        with requests.get(sys.argv[1]) as response:
            status = response.text
            print(status)
    except requests.exceptions.HTTPError as e:
        print(f"Error code: {e}")
