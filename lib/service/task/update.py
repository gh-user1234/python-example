#coding:utf-8
from service.service import Service
from repository.task import TaskRepository
from dao.database import Database
from model.user import User
from model.task import Task
from model.project import Project

class TaskUpdateService(Service):
    
    def __init__(self, **params):
        self.__params = params
        self.__repo = TaskRepository(Database())
    
    def execute(self):
        try:
            task = Task(
                self.__params["task.id"],
                None,
                None,
                None,
                self.__params["task.timelimit"],
                None,
                self.__params["task.note"],
                self.__params["task.status"],
            )
            user = User(1, None)
            self.__repo.update_task(task, user)
            
        except:
            raise

