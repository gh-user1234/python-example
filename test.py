import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lib'))
from dao.database import Database

def func1():
    from model.task import Task
    from model.user import User
    
    task = Task(None, "project1", "task3", "test task", "2015-01-01 0:00:00", "2015-01-31 0:00:00")
    user = User(1, "user1")

    db = Database()
    db.begin_trans()
    dao = TaskDao(db, task, user)
    dao.create()
    db.commit()

def func2():
    task = Task(1, None, None, None, None, None)
    user = User(1, "user1")

    db = Database()
    dao = TaskDao(db, task, user)
    record = dao.get()
    for v in record:
        print(v)

def func3():
    proj = Project(None, "project1", "test project", "2015-01-01 0:00:00", 1)
    user = User(1, "user1")

    db = Database()
    dao = ProjectDao(db, proj, user)
    db.begin_trans()
    dao.create()
    db.commit()

def func4():
    proj = Project(1, None, None, None, None)
    user = User(1, "user1")

    db = Database()
    dao = ProjectDao(db, proj, user)
    record = dao.get()
    for v in record:
        print(v)
    
def func5():
    from dao.task_serial_number_dao import TaskSerialNumberDao
    project = Project(1, "project1", "test project", "2015-01-01 0:00:00", 1)
    task    = Task(1, "project1", "task3", "test task", "2015-01-01 0:00:00", "2015-01-31 0:00:00")
    user    = User(1, "user1")

    db = Database()
    dao = TaskSerialNumberDao(db, task, project)
    db.begin_trans()
    dao.create()
    db.commit()
    print(db.last_insert_id())

    record = dao.get()
    for v in record:
        print(v)


def func6():
    from dao.task_sql import TaskSql
    from dao.task_find_dao import TaskFindDao
    
    sql = TaskSql()
    sql.where("project.name = ?")
    sql.where("task_serial_number.serial_no = ?")
    sql.where("task_log.status = 0")
    sql.order_by("task.timelimit ASC")
    sql.order_by("task_log.created ASC")
    sql.order_by("project.name ASC")
    param = ["project1", 1]

    print(sql.build())

    db = Database()
    dao = TaskFindDao(db, sql.build(), param)
    record = dao.get()
    for v in record:
        print(v)

def func7():
    from repository.task_repository import TaskRepository
    repo = TaskRepository(Database())
    task = repo.find_one("project1", 1)
    print task.get_timelimit()
"""
    record = repo.fetch_task_list()
    for v in record:
        print v
"""    
    
def func8():
    from service.task.create import TaskCreateService
    params = {
        "title" : "task88",
        "timelimit":"2015-01-01 0:00:00",
        "note":"aaaaa",
        "user_id":1,
        "project_id":1,
    }
    service = TaskCreateService(params)
    service.execute()    

def func9():
    from dao.task.task_log import TaskLogDao
    id_ = 1
    task_id = 1
    staus = 0
    note = "afasfd"
    create = "2015-01-01 0:00:00"
    created_by = 1
    db = Database()
    dao = TaskLogDao(db, id_, task_id, staus, note, create, created_by)
    dao.get()
    dao.update()
    dao.delete()
    dao.create()
    db.rollback()  









func9()
