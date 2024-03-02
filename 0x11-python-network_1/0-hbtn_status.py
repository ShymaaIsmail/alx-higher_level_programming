#!/usr/bin/python3
import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    status = response.read()
    print("Body response:")
    print(f"   - type: {type(status)}")
    print(f"   - content: {status}")
    print(f"   - utf8 content: {status.decode('utf-8')}")
