#coding:utf-8
import os
from config import Config

class LogConfig(Config):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "__instance__"):
            cls.__instance__ = super(LogConfig, cls).__new__(cls, *args, **kwargs)
        return cls.__instance__

    def __init__(self):
        super(LogConfig, self).__init__(self.__setup())
    
    def __setup(self):
        return {
            "level"      : "DEBUG",
        }

if __name__ == '__main__':
    conf = LogConfig()
    print conf.get("level")
