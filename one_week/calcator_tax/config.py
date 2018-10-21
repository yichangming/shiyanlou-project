#!/usr/bin/env python3

import os
import sys
import operator as op
import args

class Config(object):
    def __init__(self,configfile):
        self.userfile = configfile
        self._config = {}
        self.ratio = 0
        self._read_config()

    def _read_config(self):
        if os.path.exists(self.userfile) == False:
            print('{} isn\'t exist'.format(self.userfile))
            raise Exception('FileNotExist')
        with open(self.userfile) as f:
            for line in f:
                if '=' in line:
                    key,value = line.strip().split('=')
                    print(key, value)
                    self._config[key.strip()] = float(value.strip())
        for key, value in self._config.items():
            if value < 1:
                self.ratio += value

    def get_config(self, key):
        return self._config[key]

    def get_jishuL(self):
        return self._config['JiShuL']

    def get_jishuH(self):
        return self._config['JiShuH']

    def get_yanglao(self):
        return self._config['YangLao']

    def get_shiye(self):
        return self._config['ShiYe']

    def get_gongshang(self):
        return self._config('GongShang')

    def get_shengyu(self):
        return self._config('ShengYu')

    def get_gongjijin(self):
        return self._config('GongJiJin')

    def get_tax_rate(self):
        return self.ratio

if __name__ == '__main__':
    arg = args.Args(sys.argv[1:])    
    configfile = arg.get_arg('config') 
    config = Config(configfile)
    print(config.__dict__)
