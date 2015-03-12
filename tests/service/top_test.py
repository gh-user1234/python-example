import unittest
from service.top import TopService

class Test(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test1(self):
        service = TopService()
        ret = service.execute()
        project = ret["project_list"]
        
        for item in project:
            print item
        
        task = ret["task_list"]
        for item in task:
            print item

if __name__ == '__main__':
    unittest.main()
