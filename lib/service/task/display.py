#coding:utf-8
from service.service import Service
from repository.task import TaskRepository
from repository.project import ProjectRepository
from dao.database import Database

class TaskDisplayService(Service):
    def __init__(self, params):
        self.__params = params

    def execute(self):
        try:
            db = Database()
            task_repo = TaskRepository(db)
            project_repo = ProjectRepository(db)
            task = task_repo.find_one(self.__params["project_name"], self.__params["task_id"])
            if task is None:
                raise Exception("Task Not Found")
            return {"task" : task}
        except Exception as ex:
            print ex
            raise
