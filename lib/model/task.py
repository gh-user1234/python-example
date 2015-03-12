#coding:utf-8
"""
"""
class Task(object):
    def __init__(self, id_, project_name, title, serial_no, timelimit, timestamp, note, status):
        self.id_ = id_
        self.project_name = project_name
        self.title = title
        self.serial_no = serial_no
        self.timelimit = timelimit
        self.timestamp = timestamp
        self.note = note
        self.status = status

    def __str__(self):
        values = (self.id_, self.project_name, self.title, self.serial_no, self.timelimit, self.timestamp, self.note, self.status)
        return "[%s, %s, %s, %s, %s, %s, %s, %s]" % values

    def get_id(self):
        return self.id_
    
    def get_project_name(self):
        return self.project_name

    def get_serial_no(self):
        return self.serial_no

    def get_title(self):
        return  self.title

    def get_timelimit(self):
        return self.timelimit

    def get_status(self):
        return self.status

    def get_note(self):
        return self.note

    def get_created(self):
        return self.timestamp



