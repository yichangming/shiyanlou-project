#!/usr/bin/env python3

def countlines(name):
    with open(name) as file:
        count = 0
        for line in file:
            count += 1
            print(line)
        print('Lines:', count)

if __name__ == '__main__':
    filename = input("Enter the file name: ")
    countlines(filename)
