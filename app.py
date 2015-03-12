#coding:utf-8
import sys, os
import bobo

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lib'))

from controller.top import TopController
from controller.task import TaskController
from controller.project import ProjectController

if __name__ == "bobo__main__":
    pass
else:
    application = bobo.Application(bobo_resources=__name__)
