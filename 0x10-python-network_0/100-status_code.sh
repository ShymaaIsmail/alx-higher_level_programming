#!/bin/bash
# print response size 
curl  -s  -w "%{http_code}\n" -o "/dev/null" "$1"
