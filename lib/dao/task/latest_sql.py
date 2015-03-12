#coding:utf-8

class LatestTaskSQL(object):
    def __init__(self):
        self._sql = self.__setup()
        self._where = []
        self._order_by = []
    
    def __setup(self):
        sql = """
SELECT
    task.id                         as 'task_id',
    project.name                    as 'project_name',
    task_serial_number.serial_no    as 'serial_no',
    task.title                      as 'title',
    task.timelimit                  as 'timelimit',
    task_log.timestamp              as 'timestamp',
    task_log.note                   as 'note',
    task_log.status                 as 'status',
    task_log.user_id                as 'user_id'
FROM
    task INNER JOIN task_log ON(
        task.id = task_log.task_id
    ) INNER JOIN task_serial_number ON(
        task.id = task_serial_number.task_id 
    ) INNER JOIN project ON (
        project.id = task_serial_number.project_id
    ) INNER JOIN (SELECT id, MAX(timestamp) FROM task_log GROUP BY task_id) as log2 ON(
        task_log.id = log2.id
    )
WHERE
    %(where)s
ORDER BY
    %(order_by)s
"""
        return sql

    def where(self, expression):
        self._where.append(expression)
        return self
    
    def order_by(self, expression):
        self._order_by.append(expression)
        return self
    
    def build(self):
        value = {
            "where"     : " AND ".join(self._where),
            "order_by"  : " , ".join(self._order_by),
        }
        return self._sql % value

if __name__ == "__main__":
    sql = LatestTaskSQL()
    sql.where("id = ?")
    sql.where("name = ?")
    sql.order_by("name ASC")
    print(sql.build())
