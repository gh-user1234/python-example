#coding:utf-8
from dao.dao import Dao

class ProjectDao(Dao):

    def __init__(self, db, project, user):
        self.db = db
        self.project = project
        self.user = user
    
    def get(self):
        sql = "select * from project where id = ?"
        param = [self.project.get_id()]
        return self.db.execute_query(sql, param)
    
    def create(self):
        sql = """
            INSERT INTO project(
                id,
                name,
                description,
                status,
                created,
                user_id
            )VALUES(
                null,
                ?,
                ?,
                0,
                datetime('now', 'localtime'),
                ?
            )
        """
        param = [
            self.project.get_name(),
            self.project.get_description(),
            self.user.get_id(),
        ]
        self.db.execute(sql, param)
    
    def update(self):
        sql = "UPDATE project SET name = ?, description = ?, status = ? WHERE id = ?"
        param = [
            self.project.get_name(),
            self.project.get_description(),
            self.project.get_status(),
            self.project.get_id(),
        ]
        self.db.execute(sql, param)
    
    def delete(self):
        pass
