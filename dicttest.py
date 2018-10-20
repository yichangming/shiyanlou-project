#!/usr/bin/env python3

import sys
'''
dict_a = {}

for arg in sys.argv[1:]:
    key,value = arg.split(":")
    dict_a[key] = value

for key,value in dict_a.items():
    print("ID:{} Name: {}".format(key,value))
'''

output_dict = {}

def handle_data(arg):
    key,value = arg.split(":")
    output_dict[key] = value

def print_data(key,value):
    print("ID:{} Name:{}".format(key,value))

if __name__ == '__main__':

    for arg in sys.argv[1:]:
        handle_data(arg)

    for key in output_dict:
        print_data(key, output_dict[key])
