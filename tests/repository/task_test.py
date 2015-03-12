import unittest
from repository.task import TaskRepository
from dao.database import Database
from model.project import Project
from model.task import Task
from model.user import User

class Test(unittest.TestCase):
    def setUp(self):
        self.repo = TaskRepository(Database())
    
    def tearDown(self):
        pass
    
    def test1(self):
        result = self.repo.find_one("project1", 1)
        #print(result) 

    def test2(self):
        result = self.repo.fetch_task_list()
        for item in result:
            print(item)

    def test3(self):
        pass
        #task = self.repo.get_latest(1)
        #print(task)

    def test4(self):
        project = Project(1, None, None, None, None, None)
        task = Task(None, "task", None, "2015-01-31 0:00:00", None, "aaaaa", None)
        user = User(1, None)
        #self.repo.create_task(project, task, user)

    def test5(self):
        task = Task(3, "task2", None, "2015-01-31 0:00:00", None, "bbbbb", 1)
        user = User(1, None)
        #self.repo.update_task(task, user)
    
    def test6(self):
        ret = self.repo.get_latest(1)
        print ret
        
    
        

if __name__ == '__main__':
    unittest.main()
