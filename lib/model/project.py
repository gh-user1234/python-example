#coding:utf-8

"""
"""
class Project(object):
    
    def __init__(self, id_, name, description, status, created, create_user):
        self.id_ = id_
        self.name = name
        self.description = description
        self.status = status
        self.created = created
        self.create_user = create_user

    def __str__(self):
        values = (self.id_, self.name, self.description, self.status,self.created, self.create_user)
        return "[%s, %s, %s, %s, %s, %s]" % values
    
    def get_id(self):
        return self.id_
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description
    
    def get_status(self):
        return self.status

    def get_created(self):
        return self.created
    
    def get_created_user(self):
        return self.create_user
        
