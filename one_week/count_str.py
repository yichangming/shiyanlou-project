#!/usr/bin/env python3

def char_count(str):
    char_list = set(str)
    for char in char_list:
        print(char,str.count(char))

def char_count2(str):
    dict_a = {}
    for i in str:
        if i not in dict_a.keys():
            dict_a[i] = 1
        else:
            dict_a[i] += 1
    print(dict_a)

def char_count3(str):
    countdict = {}
    for char in str:
        countdict[char] = countdict.get(char,0) + 1
    for (keys,values) in countdict.items():
        print(keys,values)

if __name__ == '__main__':

    s = input("Enter a string:")
    char_count3(s)
