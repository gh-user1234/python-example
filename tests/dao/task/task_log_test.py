import unittest
from dao.database import Database
from dao.task.task_log import TaskLogDao


class Test(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test1(self):
        id_ = 1
        task_id = 1
        staus = 0
        note = "afasfd"
        create = "2015-01-01 0:00:00"
        created_by = 1
        db = Database()
        dao = TaskLogDao(db, id_, task_id, staus, note, create, created_by)
        dao.create()
        db.rollback()
        self.assertTrue(True)

    def test2(self):
        id_ = 1
        task_id = 1
        staus = 0
        note = "afasfd"
        create = "2015-01-01 0:00:00"
        created_by = 1
        db = Database()
        dao = TaskLogDao(db, id_, task_id, staus, note, create, created_by)
        record = dao.get()
        print(record)

if __name__ == '__main__':
    unittest.main()
