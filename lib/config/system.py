#coding:utf-8
import os
from config import Config

class SystemConfig(Config):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "__instance__"):
            cls.__instance__ = super(SystemConfig, cls).__new__(cls, *args, **kwargs)
        return cls.__instance__

    def __init__(self):
        super(SystemConfig, self).__init__(self.__setup())

    def __setup(self):
        home = os.path.realpath(os.path.join(os.path.abspath(os.path.dirname(__file__)), "../../"))
        return {
            "home"      : home,
            "templates" : os.path.join(home, "templates"),
            "tmp"       : os.path.join(home, "var/tmp"),
            "log"       : os.path.join(home, "var/log/app.log"),
            "db"        : os.path.join(home, "var/db/task.db"),
        }

if __name__ == '__main__':
    conf = SystemConfig()
    print conf.get("templates")
    print conf.get("log")
