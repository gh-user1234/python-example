import unittest
from dao.database import Database
from dao.task.task import TaskDao

class Test(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test1(self):
        db = Database()
        dao = TaskDao(db, 1, None, None)
        record = dao.get()
        print record
        
    def test2(self):
        db = Database()
        record = db.execute_query("SELECT id, task_id, MAX(timestamp) FROM task_log GROUP BY task_id", [])
        print(record)

    def test3(self):
        db = Database()
        record = db.execute_query("SELECT * FROM task_log", [])
        for item in record:
            print(item)


if __name__ == '__main__':
    unittest.main()
