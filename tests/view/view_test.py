#coding:utf-8
import unittest
from view.view import View

class Test(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test1(self):
        params = {
            "template.name":"ERROR",
            "id":1,
            "user_name":"user1",
        }
        view = View(**params)
        print view.render()
        self.assertTrue(True)

    """
    paramsにtemplate.nameが無い場合（エラーが発生することを確認）
    """
    def test2(self):
        try:
            params = {
                "id":1,
                "user_name":"user1",
            }
            view = View(**params)
            print view.render()
            self.assertTrue(False)
        except Exception as ex:
            print "Error %s" % ex
            self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
