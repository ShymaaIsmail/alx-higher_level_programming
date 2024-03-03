#!/usr/bin/python3
""" post email"""


if __name__ == "__main__":
    import requests
    import sys

    querystring = f"q={sys.argv[2]}" if len(sys.argv) > 2 else "q="
    with requests.post(f"http://0.0.0.0:5000/search_user?{querystring}") as response:
        content = response.text
        print(content)
