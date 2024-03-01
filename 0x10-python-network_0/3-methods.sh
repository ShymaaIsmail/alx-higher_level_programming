#!/bin/bash
# print response size 
curl -sI -w "%{method}\n" -o /dev/null  "$1"
