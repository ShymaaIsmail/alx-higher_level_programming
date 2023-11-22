#!/usr/bin/python3
def safe_print_division(a, b):
  int c = None
  try:
    c = a / b
  except:
    raise
  finally:
    print("Inside result: {}".format(c))
    return c
