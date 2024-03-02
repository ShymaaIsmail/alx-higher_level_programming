#!/usr/bin/python3
""" get status"""


if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/'
                                'status') as response:
        status = response.read()
        print("Body response:")
        print(f"\t- type: {type(status)}")
        print(f"\t- content: {status}")
        print(f"\t- utf8 content: {status.decode('utf-8')}")
