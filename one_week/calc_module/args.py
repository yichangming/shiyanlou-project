#!/usr/bin/env python3

import sys

class Args(object):

    def __init__(self,_argv):
        self.args = _argv
        self.argv = {}
        self._read_args()

    def _read_args(self):
        try:
            index = self.args.index('-c')
            self.argv['config'] = self.args[index + 1]
            index = self.args.index('-d')
            self.argv['userdata'] = self.args[index + 1]
            index = self.args.index('-o')
            self.argv['out'] = self.args[index + 1] 
        #except (IndexError, ValueError) as err:
        except:        
            print('Error use -c configfile -d userdata')
            raise Exception("Parament Error")

    def get_arg(self,key):
        return self.argv[key]

if __name__ == '__main__':
    arg = Args(sys.argv[1:])
    print(arg.__dict__)
