#!/usr/bin/python3
""" get header"""


if __name__ == "__main__":
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers["X-Request-Id"])
