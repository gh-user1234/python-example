import unittest
from service.project.create import ProjectCreateService

class Test(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test1(self):
        params = {
            "project_id":1,
            "user_id":1,
            "title":"task1",
            "timelimit":"2015-01-31 23:59:59",
            "note":"test!"
        }
        service = ProjectCreateService(**params)
        service.execute()


if __name__ == '__main__':
    unittest.main()
