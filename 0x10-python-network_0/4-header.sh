#!/bin/bash
# print response size 
curl -sI -X GET -H "X-School-User-Id: 98" "$1"
