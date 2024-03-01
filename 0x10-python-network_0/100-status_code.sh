#!/bin/bash
# print response size 
curl  -s -L -w "%{http_code}\n" -o "/dev/null" "$1"
