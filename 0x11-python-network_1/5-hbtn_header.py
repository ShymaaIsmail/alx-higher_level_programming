#!/usr/bin/python3
""" get header"""


if __name__ == "__main__":
    import requests
    import sys

    with requests.get(sys.argv[1]) as response:
        print(response.headers["X-Request-Id"])
