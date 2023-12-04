#!/usr/bin/python3
import sys


Rectangle = __import__('9-rectangle').Rectangle

r = Rectangle(sys.maxsize, sys.maxsize)

print(r)
print(r.area())
