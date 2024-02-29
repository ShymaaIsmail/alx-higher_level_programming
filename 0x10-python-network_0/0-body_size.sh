#!/bin/bash
# print response size 
curl  -s  -w "%{size_header}\n" -o "/dev/null" "$1"
