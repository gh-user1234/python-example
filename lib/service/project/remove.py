#coding:utf-8
from service.service import Service
from repository.project import ProjectRepository
from exception.exceptions import ApplicationError

class ProjectRemoveService(Service):
    def __init__(self, param):
        self.__param = param

    def execute(self):
        try:
            raise Exception("Error!!")
            repo = ProjectRepository(Database())
            repo.delete_project()
        except Exception as e:
            raise

if __name__ == "__main__":
    obj = ProjectRemoveService({"project_id": 1})
    obj.execute()
