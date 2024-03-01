#!/bin/bash
# print response size 
curl  -sLw "%{http_code}\n" -o "/dev/null" "$1"
