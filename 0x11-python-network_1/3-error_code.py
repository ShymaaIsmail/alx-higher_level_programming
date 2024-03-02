#!/usr/bin/python3
""" get status"""


if __name__ == "__main__":
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as response:
        status = response.read()
        print(f"Error code: {status.decode('utf-8')}")
