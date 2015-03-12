#coding:utf-8
import os
from config import Config
from system import SystemConfig

class TemplateConfig(Config):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "__instance__"):
            cls.__instance__ = super(TemplateConfig, cls).__new__(cls, *args, **kwargs)
        return cls.__instance__

    def __init__(self):
        super(TemplateConfig, self).__init__(self.__setup())

    def __setup(self):
        conf = SystemConfig()
        dir_ =  conf.get("templates")
        return {
            "TOP"  : os.path.join(dir_, "index.html"),
            "TASK_DETAIL" : os.path.join(dir_, "task_detail.html"),
            "TASK_CREATE": os.path.join(dir_, "task_create.html"),
            "ERROR": os.path.join(dir_, "error.html"),
            "PROJECT_VIEW": os.path.join(dir_, "error.html"),
        }

if __name__ == '__main__':
    conf = TemplateConfig()
    print conf.get("TASK")
