#!/usr/bin/python3
""" get status"""


if __name__ == "__main__":
    import requests

    with requests.get('https://alx-intranet.hbtn.io/'
                        'status') as response:
        print("Body response:")
        print(f"\t- type: {type(response.text)}")
        print(f"\t- content: {response.text}")
