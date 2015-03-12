#coding:utf-8

"""Model of Session
"""
class Session(object):
    
    def __init__(self, **data):
        self.data = data
        
    def get_session_id(self):
        return self.data["session_id"]


    def get_user_id(self):
        return self.data["user_id"]

    
    def is_login(self):
        if self.data["status"] == 0:
            return False
        else:
            return True

    def change_status(self):
        pass


    def to_string(self):
        return self.data
