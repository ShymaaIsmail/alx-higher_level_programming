#!/usr/bin/python3
""" post email"""


if __name__ == "__main__":
    import requests
    import sys

    data = {'email': sys.argv[2]}
    with requests.post(sys.argv[1], data) as response:
        content = response.text
        print(content)
