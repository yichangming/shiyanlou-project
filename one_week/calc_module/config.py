#!/usr/bin/env python3

import os
import sys
import operator as op
import args
import configparser

class Config(object):
    def __init__(self,configfile,cityname):
        self.userfile = configfile
        self._config = {}
        self.ratio = 0
        self.city = cityname.upper()
        self._read_config()

    def _read_config(self):
        if os.path.exists(self.userfile) == False:
            print('{} isn\'t exist'.format(self.userfile))
            raise Exception('FileNotExist')
        config = configparser.ConfigParser()
        config.read(self.userfile)
        if self.city in config:
            params = config.items(self.city)
        else:
            params = config.items('DEFAULT')
        for item in params:
            key,value = item
            print(key,value)
            self._config[key] = float(value)
            if self._config[key.lower()] < 1:
                self.ratio += self._config[key]
        '''
        with open(self.userfile) as f:
            config = configparser.ConfigParser()
            for line in f:
                if '=' in line:
                    key,value = line.strip().split('=')
                    print(key, value)
                    self._config[key.strip()] = float(value.strip())
        for key, value in self._config.items():
            if value < 1:
                self.ratio += value
        '''
    def get_config(self, key):
        return self._config[key.lower()]

    def get_jishuL(self):
        return self._config['JiShuL'.lower()]

    def get_jishuH(self):
        return self._config['JiShuH'.lower()]

    def get_yanglao(self):
        return self._config['YangLao'.lower()]

    def get_shiye(self):
        return self._config['ShiYe'.lower()]

    def get_gongshang(self):
        return self._config['GongShang'.lower()]

    def get_shengyu(self):
        return self._config['ShengYu'.lower()]

    def get_gongjijin(self):
        return self._config['GongJiJin'.lower()]

    def get_tax_rate(self):
        return self.ratio

if __name__ == '__main__':
    arg = args.Args(sys.argv[1:])    
    configfile = arg.get_arg('config') 
    config = Config(configfile)
    print(config.__dict__)
