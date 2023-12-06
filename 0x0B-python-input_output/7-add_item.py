#!/usr/bin/python3
"""
_summary_

7-add_item
module doc
"""


import os
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file_name = "add_item.json"
args = sys.argv[1:]
saved_json = []
if os.path.exists(file_name):
    saved_json = load_from_json_file(file_name)
for item in args:
    saved_json.append(item)
if os.path.exists(file_name):
    with open(file_name, "r+", encoding="utf-8") as f:
        f.truncate(0)
save_to_json_file(saved_json, file_name)
