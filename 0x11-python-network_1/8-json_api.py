#!/usr/bin/python3
""" post email"""


if __name__ == "__main__":
    import requests
    import sys

    querystring = sys.argv[1] if len(sys.argv) >= 2 else ""
    with requests.post("http://0.0.0.0:5000/search_user",
                       data={'q': querystring}) as response:
        try:
            data = response.json()
            if data:
                print("[{}] {}".format(data.get('id'), data.get('name')))
            else:
                print("No result")
        except ValueError as v:
            print("Not valid Json")
