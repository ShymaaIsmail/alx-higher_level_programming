#!/bin/bash
# print response size 
curl -sI "$1" | grep "Allow" | cut -d " " -f2-
