#!/usr/bin/python3
""" post email"""


if __name__ == "__main__":
    import urllib.request
    import sys

    data = {'email': sys.argv[2]}
    data = data.encode('ascii')
    request = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(request) as response:
        content = response.read()
        print(content.decode('utf-8'))
