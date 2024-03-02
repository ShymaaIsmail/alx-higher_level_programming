#!/usr/bin/python3
""" post email"""


if __name__ == "__main__":
    import urllib.request
    import sys

    data = {'email': sys.argv[2]}
    request = {'method': 'POST', 'url': sys.argv[1], 'data': data}
    with urllib.request.urlopen(request) as response:
        content = response.read()
        print({content.decode('utf-8')})

