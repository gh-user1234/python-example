#coding:utf-8
from dao.session.session import SessionDao
from model.session import Session
"""Session Repository
"""
class SessionRepository(object):
    
    def __init__(self):
        pass

    def find_by_session_id(self, session_id):
        session = Session({"session_id":session_id})
        dao = SessionDao(session)
        result = dao.get()
        return Session(result)

    def create(self, session):
        dao = SessionDao(session)
        dao.create()

    def update(self, session):
        dao = SessionDao(session)
        dao.update()

    def delete(self, session):
        dao = SessionDao(session)
        dao.delete()
