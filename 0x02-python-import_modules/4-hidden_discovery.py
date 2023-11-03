#!/usr/bin/python3
from hidden_4 import hidden_4
if __name__ == "__main__":
    for mod_name in dir(hidden_4):
        if not mod_name.startswith('__'):
            print("{}".format(mod_name))
