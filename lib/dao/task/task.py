#coding:utf-8
from dao.dao import Dao

class TaskDao(Dao):

    def __init__(self, db, id_, title, timelimit):
        self.db = db
        self.id_ = id_
        self.title = title
        self.timelimit = timelimit
    
    def get(self):
        sql = "select * from task where id = ?"
        param = [self.id_]
        return self.db.execute_query(sql, param)
    
    def create(self):
        sql = """
            INSERT INTO task(
                id,
                title,
                timelimit
            )VALUES(
                null,
                ?,
                ?
            )
        """
        param = [
            self.title,
            self.timelimit,
        ]
        return self.db.execute_query(sql, param)
    
    def update(self):
        sql = "UPDATE task SET title = ?, timelimit = ? WHERE id = ?"
        param = [
            self.id_,
            self.title,
            self.timelimit,
        ]
        return self.db.execute_query(sql, param)
    
    def delete(self):
        pass


