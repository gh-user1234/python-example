#coding:utf-8
from exception.exceptions import ProjectNotFoundError
from dao.database import Database
from dao.project.project import ProjectDao
from dao.project.find import ProjectFindDao
from dao.project.sql import ProjectSQL
from model.project import Project
"""
"""
class ProjectRepository(object):

    def __init__(self, db):
        self.__db = db

    def find_by_id(self, id_):
        sql = ProjectSQL()
        sql.where("id = ?")
        sql.order_by("name ASC")
        dao = ProjectFindDao(self.__db, sql.build(), [id_])
        record = dao.get()

        if len(record) == 0:
            raise ProjectNotFoundError()

        return Project(
            record[0]["id"],
            record[0]["name"],
            record[0]["description"],
            record[0]["status"],
            record[0]["created"],
            record[0]["user_id"]
        )

    def find_by_name(self, name):
        sql = ProjectSQL()
        sql.where("name = ?")
        sql.order_by("name ASC")
        dao = ProjectFindDao(self.__db, sql.build(), [name])
        record = dao.get()

        if len(record) == 0:
            raise ProjectNotFoundError()

        return Project(
            record[0]["id"],
            record[0]["name"],
            record[0]["description"],
            record[0]["status"],
            record[0]["created"],
            record[0]["user_id"]
        )

    def fetch_all(self):
        sql = ProjectSQL()
        sql.where("0 = 0")
        sql.order_by("name ASC")
        dao = ProjectFindDao(self.__db, sql.build(), [])
        record = dao.get()
        result = []
        for item in record:
            _ =  Project(
                item["id"],
                item["name"],
                item["description"],
                item["status"],
                item["created"],
                item["user_id"]
            )
            result.append(_)
        return result

    def add_project(self, project, user):
        dao = ProjectDao(self.__db, project, user)
        self.__db.begin_trans()
        dao.create()
        self.__db.commit()

    def update_project(self, project, user):
        dao = ProjectDao(self.__db, project, user)
        self.__db.begin_trans()
        dao.update()
        self.__db.commit()

    def delete_project(self, project):
        dao = ProjectDao(self.__db, project, user)
        self.__db.begin_trans()
        dao.delete()
        self.__db.commit()
