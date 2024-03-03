#!/usr/bin/python3
""" get my github id"""


if __name__ == "__main__":
    import requests
    import sys

    github_headers = {"Accept": "application/vnd.github+json",
                      "Authorization": f"Bearer {sys.argv[2]}",
                      "X-GitHub-Api-Version": "2022-11-28"}
    with requests.get(f"https://api.github.com/users/{sys.argv[1]}",
                      headers=github_headers) as response:
        try:
            profile_data = response.json()
            print(profile_data["id"])
        except Exception:
            print("None")
