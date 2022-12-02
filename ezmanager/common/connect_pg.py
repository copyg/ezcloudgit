from fileinput import close
from sqlite3 import Cursor
import psycopg2

dbinfo = {
    "host": "192.168.80.119",
    "user": "postgres",
    "password": "password",
    "port": 30004
}


class DbConnectPg():

    def __init__(self,  database="x"):
        self.db = psycopg2.connect(database=database, 
						**dbinfo)
    # 使用cursor()方法获取操作游标
        self.cursor = self.db.cursor()

    def select(self, pg):
    # SQL 查询语句
    #  sql = "SELECT * FROM EMPLOYEE \
    #         WHERE INCOME > %s" % (1000)
        self.cursor.execute(pg)
        results = self.cursor.fetchall()# 返回全部
        # 返回具体值
        r= results[0][0]
        return r

    def execute(self, pg):
    # SQL 删除、提交、修改语句
    #  sql = "DELETE FROM EMPLOYEE WHERE AGE > %s" % (20)
        try:
    # 执行SQL语句
            self.cursor.execute(pg)           # 提交修改
            self.db.commit()
        except:
        # 发生错误时回滚
            self.db.rollback()

    def close(self):
    # 关闭连接
        self.db.close()
if __name__ == '__main__':
    db = DbConnectPg(database="ezmanager")
    sql = 'SELECT count(*) FROM "ezpro"."meeting" WHERE "id" = 146192 LIMIT 1000 OFFSET 0'
    a = db.select(sql)
    print(a)

    #sql = 'SELECT id, goodscode from apiapp_goods WHERE goodscode = "sp_20211018";'



