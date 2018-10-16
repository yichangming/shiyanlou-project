#!/usr/bin/env python3

import sys

dict_a = {}

for arg in sys.argv[1:]:
    key,value = arg.split(":")
    dict_a[key] = value

for key,value in dict_a.items():
    print("ID:{} Name: {}".format(key,value))
