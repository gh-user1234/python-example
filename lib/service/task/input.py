#coding:utf-8
from service.service import Service
from service.result import ServiceResult
from repository.task_repository import TaskRepository
from dao.database import Database
from model.user import User
from model.task import Task
from model.project import Project

class TaskInputService(Service):
    def __init__(self, params):
        self.params = params
        self.result = ServiceResult()
        db = Database()
        self.task_repo = TaskRepository(db)
        self.project_repo = ProjectRepository(db)


    def execute(self):
        list_ = self.project_repo.get_project_list()
        self.result.set("project_list", list_)
        return self.result
