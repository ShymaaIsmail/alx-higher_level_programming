#!/bin/bash
# print response size 
curl  -sLw "%{http_code}" -o "/dev/null" "$1"
