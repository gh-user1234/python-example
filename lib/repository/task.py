#coding:utf-8
from exception.exceptions import TaskNotFoundError
from dao.task.sql import TaskSQL
from dao.task.latest_sql import LatestTaskSQL
from dao.task.task_find import TaskFindDao
from dao.task.task import TaskDao
from dao.task.task_log import TaskLogDao
from dao.task.serial_number import TaskSerialNumberDao
from model.task import Task
from model.user import User


class TaskRepository(object):
    
    def __init__(self, db):
        self.db = db

    def find_one(self, project_name, serial_no):
        sql = LatestTaskSQL()
        sql.where("project.name = ?")
        sql.where("task_serial_number.serial_no = ?")
        sql.where("task_log.status = 1")
        sql.order_by("task.timelimit ASC")
        sql.order_by("task_log.timestamp ASC")
        sql.order_by("project.name ASC")
        param = [project_name, serial_no]

        dao = TaskFindDao(self.db, sql.build(), param)
        record = dao.get()
        
        if len(record) == 0:
            return None
             
        for item in record:
            return Task(
                item["task_id"],
                item["project_name"],
                item["title"],
                item["serial_no"],
                item["timelimit"],
                item["timestamp"],
                item["note"],
                item["status"]
            )

    def fetch_all(self):
        sql = LatestTaskSQL()
        sql.where("task_log.status = 1")
        sql.order_by("task.timelimit ASC")
        sql.order_by("task_log.timestamp ASC")
        sql.order_by("project.name ASC")
        
        dao = TaskFindDao(self.db, sql.build(), [])
        record = dao.get()
        result = []
        
        for item in record:
            _ = Task(
                item["task_id"],
                item["project_name"],
                item["title"],
                item["serial_no"],
                item["timelimit"],
                item["timestamp"],
                item["note"],
                item["status"]
            )
            result.append(_)
            
        return result

    def get_latest(self, task_id):
        sql = LatestTaskSQL()
        sql.where("task.id = ?")
        sql.order_by("task.timelimit ASC")
        sql.order_by("task_log.timestamp ASC")
        sql.order_by("project.name ASC")
        
        dao = TaskFindDao(self.db, sql.build(), [task_id])
        record = dao.get()
        result = []
        
        for item in record:
            return Task(
                item["project_name"],
                item["task_id"],
                item["title"],
                item["serial_no"],
                item["timelimit"],
                item["timestamp"],
                item["note"],
                item["status"]
            )
            result.append(_)
        
        raise TaskNotFoundError("Task NotFound")
        

    def create_task(self, project, task, user):
        try:
            #== BEGIN TRANSACTION ==
            self.db.begin_trans()
            #== entry:task ==
            task_dao = TaskDao(self.db, None, task.get_title(), task.get_timelimit())
            task_dao.create()
            #== entry:task_log ==
            id_ = self.db.last_insert_id()
            tasklog_dao = TaskLogDao(self.db, None, id_, None, task.get_note(), 1, user.get_id())
            tasklog_dao.create()
            #== entry:task_serial_number ==
            no_dao = TaskSerialNumberDao(self.db, None, None, project.get_id(), id_)
            no_dao.create()
            #== COMMIT ==
            self.db.commit()

        except:
            self.db.rollback()
            raise

    def update_task(self, task, user):
        try:
            dao = TaskLogDao(self.db, None, task.get_id(), None, task.get_note(), task.get_status(), user.get_id())
            self.db.begin_trans()
            dao.create()
            self.db.commit()

        except:
            self.db.rollback()
            raise

    def modify_task(self, task):
        try:
            task_dao = TaskDao(self.db, task.get_id(), task.get_title(), task.get_timelimit())
            self.db.begin_trans()
            task_dao.update()
            self.db.commit()

        except:
            self.db.rollback()
            raise
    
    def modify_tasklog(self, tasklog):
        try:
            task_dao = TaskDao(self.db, tasklog.get_id(), tasklog.get_task_id(), tasklog.get_status(), tasklog.get_note(), None, user.get_id())
            self.db.begin_trans()
            task_dao.update()
            self.db.commit()

        except:
            self.db.rollback()
            raise


    def delete(self, task):
        pass

