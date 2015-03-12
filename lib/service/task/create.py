#coding:utf-8
from service.service import Service
from repository.task import TaskRepository
from dao.database import Database
from model.user import User
from model.task import Task
from model.project import Project

class TaskCreateService(Service):
    
    def __init__(self, **params):
        self.__params = params
        self.__repo = TaskRepository(Database())
    
    def execute(self):
        try:
            project = Project(1, None, None, None, None, None)
            task = Task(None, None, self.__params["task.title"], None, self.__params["task.timelimit"], None, self.__params["task.note"], 1)
            user = User(self.__params["user.id"], None)
            self.__repo.create_task(project, task, user)
            
        except:
            raise

