#!/usr/bin/python3
""" get status"""


if __name__ == "__main__":
    import urllib.request
    import sys

    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            status = response.read()
            print(status.decode('utf-8'))
    except urllib.error.URLError as e:
        print(f"Error code: {e}")
