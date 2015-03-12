import unittest
from service.task.create import TaskCreateService

class Test(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test1(self):
        params = {
            "project.id":1,
            "user.id":1,
            "task.title":"task999",
            "task.timelimit":"2015-12-31 23:59:59",
            "task.note":"test!!",
        }
        service = TaskCreateService(**params)
        service.execute()


if __name__ == '__main__':
    unittest.main()
