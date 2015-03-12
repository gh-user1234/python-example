#coding:utf-8

"""
"""
class User(object):
    def __init__(self, id_, name):
        self.id_ = id_
        self.name = name
    
    def get_id(self):
        return self.id_

    def get_name(self):
        return self.name

if __name__ == '__main__':
    id_ = "1"
    name = "user1"
    task = User(id_, name)
    print task.get_id()
    print task.get_name()
