#!/usr/bin/env python3

import os
import sys
import operator as op

class Config(object):
    def __init__(self,configfile):
        if os.path.exists(configfile) == False:
            print('{} isn\'t exist'.format(configfile))
            sys.exit()
        self._config = {}
        with open(configfile) as f:
            for line in f:
                key,value = line.strip().split('=')
                self._config[key] = value

    def get_config(self, key):
        return self._config[key]

if __name__ == '__main__':
    if (len(sys.argv) != 3) or (op.eq(sys.argv[1], '-c') == False):
        print('please input: -c filename')
        sys.exit()
    config = Config(sys.argv[2])
    print(config.__dict__)
