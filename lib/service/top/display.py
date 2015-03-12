#coding:utf-8
from service.service import Service
from dao.database import Database
from repository.task import TaskRepository
from repository.project import ProjectRepository

class TopDisplayService(Service):
    def __init__(self):
        pass

    def execute(self):
        db = Database()
        task_repo = TaskRepository(db)
        project_repo = ProjectRepository(db)
        return {
            "task_list" : task_repo.fetch_all(),
            "project_list" : project_repo.fetch_all(),
        }
