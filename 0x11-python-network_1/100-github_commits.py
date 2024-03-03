#!/usr/bin/python3
""" get github last 10 commits"""


if __name__ == "__main__":
    import requests
    import sys

    headers = {"Accept": "application/vnd.github.VERSION.sha"}
    with requests.get(f"https://api.github.com/repos/"
                      "{sys.argv[2]}/{sys.argv[1]}/commits/master",
                      headers=headers) as response:
        try:
            commits = response.json()
            print(commits)
        except Exception:
            print("None")
