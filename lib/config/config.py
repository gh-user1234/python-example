#coding:utf-8

class Config(object):
    def __init__(self, conf):
        self.__conf = conf

    def get(self, key):
        return self.__conf[key]
