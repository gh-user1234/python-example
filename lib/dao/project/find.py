#coding:utf-8
from dao.dao import Dao

class ProjectFindDao(Dao):

    def __init__(self, db, sql, params):
        self.db = db
        self.sql = sql
        self.params = params
    
    def get(self):
        return self.db.execute_query(self.sql, self.params)
