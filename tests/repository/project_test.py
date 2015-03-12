import unittest
from repository.project import ProjectRepository
from dao.database import Database
from model.project import Project
from model.user import User

class Test(unittest.TestCase):
    def setUp(self):
        self.repo = ProjectRepository(Database())
    
    def tearDown(self):
        pass
    
    def test1(self):
        result = self.repo.find_by_id(1)
        print(result)

    def test2(self):
        result = self.repo.fetch_all()
        for item in result:
            print(item)

    def test3(self):
        prj = Project(None, "project1", "test", None, None, None)
        user = User(1, "user1")
        #self.repo.add_project(prj, user)

    def test4(self):
        prj = Project(1, "project99", "test", 0, None, None)
        user = User(1, "user1")
        self.repo.update_project(prj, user)

if __name__ == '__main__':
    unittest.main()
