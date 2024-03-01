#!/bin/bash
# print response size 
curl -s -w "%{method}\n" -o /dev/null  "$1"
