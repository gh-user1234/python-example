#coding:utf-8
from service.service import Service
from repository.project import ProjectRepository


class ProjectCreateService(Service):
    def __init__(self, **kwargs):
        self.__kwargs = kwargs

    def execute(self):
        for key in self.__kwargs:
            print self.__kwargs[key]
