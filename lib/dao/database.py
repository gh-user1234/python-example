#coding:utf-8

import sqlite3
from config.factory import ConfigFactory

class Database(object):
    """sqlite3 wrapper 
    """
    def __init__(self):
        conf = ConfigFactory.createSystemConfig()
        #'DEFERRED', 'IMMEDIATE', 'EXCLUSIVE'
        self.connection = sqlite3.connect(conf.get('db'), isolation_level='DEFERRED')
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

    def execute_query(self, sql, param=[]):
        self.cursor.execute(sql, param)
        return self.cursor.fetchall()

    def execute(self, sql, param=[]):
        self.cursor.execute(sql, param)

    def last_insert_id(self):
        return self.cursor.lastrowid

    def begin_trans(self):
        self.execute("BEGIN TRANSACTION", [])

    def commit(self):
        self.connection.commit()

    def rollback(self):
        self.connection.rollback()
