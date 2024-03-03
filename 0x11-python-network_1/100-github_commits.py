#!/usr/bin/python3
""" get github last 10 commits"""


if __name__ == "__main__":
    import requests
    import sys

    headers = {"Accept": "application/vnd.github+json"}
    params = {"per_page": 10}
    user = sys.argv[2]
    repo = sys.argv[1]

    with requests.get(f"https://api.github.com/repos/{user}/{repo}/commits",
                      headers=headers, params=params) as response:
        try:
            commits = response.json()
            for commit in commits:
                print(f"{commit['sha']}: {commit['commit']['author']['name']}")
        except Exception:
            print("None")
