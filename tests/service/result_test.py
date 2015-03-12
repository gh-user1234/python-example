import unittest
from service.result import ServiceResult

class Test(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test1(self):
        result = ServiceResult()
        result.set("key", "value")
        self.assertEqual(result.get("key"), "value")
        print(result.get("key"))

if __name__ == '__main__':
    unittest.main()
