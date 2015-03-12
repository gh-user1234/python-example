#coding:utf-8
from dao.dao import Dao

class TaskLogDao(Dao):
    def __init__(self, db, id_, task_id, timestamp, note, staus, create_user):
        self.db = db
        self.id_ = id_
        self.task_id = task_id
        self.timestamp = timestamp
        self.note = note
        self.staus = staus
        self.create_user = create_user

    def get(self):
        sql = """
            SELECT
                *
            FROM
                task_log
            WHERE
                task_id = ?
            ORDER BY
                task_id ASC,
                timestamp ASC
        """
        param = [self.task_id]
        return self.db.execute_query(sql, param)


    def create(self):
        sql ="""
            INSERT INTO task_log(
                id,
                task_id,
                timestamp,
                note,
                status,
                user_id
            )VALUES(
                null,
                ?,
                datetime('now', 'localtime'),
                ?,
                ?,
                ?
            )
        """
        param = [
            self.task_id,
            self.note,
            self.staus,
            self.create_user,
        ]
        self.db.execute(sql, param)

    def update(self):
        pass
    
    def delete(self):
        pass


