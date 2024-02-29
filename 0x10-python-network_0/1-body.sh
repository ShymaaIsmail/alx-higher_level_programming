#!/bin/bash
# print response size 
response=$(curl  -s  -w "%{http_code}"  "$1")
status="${response: -3}"
if [ "$status" = "200" ]; then
    response_body=$(echo "$response" | sed '$s/...$//')
    echo "$response_body"
fi
