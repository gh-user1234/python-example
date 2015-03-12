#coding:utf-8
class ProjectSQL(object):
    def __init__(self):
        self._sql = self.__setup()
        self._where = []
        self._order_by = []
    
    def __setup(self):
        sql = """
SELECT
    id,
    name,
    description,
    status,
    created,
    user_id
FROM
    project
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
            "order_by"  : ", ".join(self._order_by),
        }
        return self._sql % value

if __name__ == "__main__":
    sql = ProjectSQL()
    sql.where("id = ?")
    sql.where("name = ?")
    sql.order_by("name ASC")
    print(sql.build())
