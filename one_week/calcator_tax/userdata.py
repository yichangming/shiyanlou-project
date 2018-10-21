#!/usr/bin/env python3

import sys
import csv
import args
import os

class UserData(object):

    def __init__(self,usrfile):
        self.userfile = usrfile
        self.usrdata = []
        self._read_file()

    def _read_file(self):
        if os.path.exists(self.userfile) == False:
            print('{} isn\'t exist'.format(self.userfile))
            raise Exception('FileNotExist')        
        with open(self.userfile) as f:
                self.userdata = list(csv.reader(f))

    def get_users(self):
        return self.userdata

if __name__ == '__main__':
    arg = args.Args(sys.argv[1:])
    userdatafile = arg.get_arg('userdata')
    userinfo = UserData(userdatafile)
    print(userinfo.__dict__)
                   
