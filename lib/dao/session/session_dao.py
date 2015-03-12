#coding:utf-8
from dao.dao import Dao

class SessionDao(object):
    
    def __init__(self, session):
        self.session = session
    
    def get(self):
        session_id = session.get_session_id()
        return {
            "session_id" : session_id,
            "user_id"    : 1,
            "status"     : 1,
            "last_login" : "2015-01-01 0:00:00"
        }

    def create(self, key, value):
        return {}

    def update(self):
        pass

    def delete(self):
        pass

if __name__ == "__main__":
    dict_ =  {
        "session_id" : session_id,
        "user_id"    : 1,
        "status"     : 1,
        "last_login" : "2015-01-01 0:00:00",
    }
    
    for k,v in dict_.items():
        print k
        print v

    
    
    
