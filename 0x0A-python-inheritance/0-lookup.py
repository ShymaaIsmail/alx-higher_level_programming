#!/usr/bin/python3
def lookup(obj):
  list = []
  if obj:
    list = dir(obj)
  return list
