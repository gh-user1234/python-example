#coding:utf-8
from dao.dao import Dao

class TaskSerialNumberDao(Dao):

    def __init__(self, db, id_, serial_no, project_id, task_id):
        self.db = db
        self.id_ = id_
        self.serial_no = serial_no
        self.project_id = project_id
        self.task_id = task_id
    
    def get(self):
        sql = "SELECT * FROM task_serial_number"
        param = []
        return self.db.execute_query(sql, param)
        

    def create(self):
        sql = """
            INSERT INTO task_serial_number
            SELECT
                null,
                ((SELECT COUNT(*) FROM task_serial_number WHERE project_id = ?) + 1),
                ?,
                ?
        """
        param = [
            self.project_id,
            self.project_id,
            self.task_id,
        ]
        self.db.execute(sql, param)
    
    def update(self):
        pass
    
    def delete(self):
        pass


