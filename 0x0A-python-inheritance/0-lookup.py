#!/usr/bin/python3
def lookup(obj):
  list = []
  if obj not None:
    list = dir(obj)
  return list
