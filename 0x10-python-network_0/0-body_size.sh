#!/bin/bash
# print response size 
curl  -s  -w "%{size_download}\n" -o "/dev/null" "$1"
