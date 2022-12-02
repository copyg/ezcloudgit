import pymysql


dbinfo = {
    "host": "192.168.80.119",
    "user": "postgres",
    "password": "password",
    "port": 30004,

}


class DbConnect():

    def __init__(self, db_cof, database="x"):
        self.db_cof = db_cof        # 打开数据库连接
        self.db = pymysql.connect(database=database,
                                  cursorclass=pymysql.cursors.DictCursor,
                                  **db_cof)
    # 使用cursor()方法获取操作游标
        self.cursor = self.db.cursor()

    def select(self, sql):
    # SQL 查询语句
    #  sql = "SELECT * FROM EMPLOYEE \
    #         WHERE INCOME > %s" % (1000)
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results

    def execute(self, sql):
    # SQL 删除、提交、修改语句
    #  sql = "DELETE FROM EMPLOYEE WHERE AGE > %s" % (20)
        try:
    # 执行SQL语句
            self.cursor.execute(sql)           # 提交修改
            self.db.commit()
        except:
        # 发生错误时回滚
            self.db.rollback()

    def close(self):
    # 关闭连接
        self.db.close()
if __name__ == '__main__':
    db = DbConnect(dbinfo,database="postgres")

    #sql = 'SELECT id, goodscode from apiapp_goods WHERE goodscode = "sp_20211018";'
    sql = 'SELECT * FROM "ezpro"."meeting_stat_location" WHERE "id" = "7015314";'
    a = db.select(sql)
    db.close()
    print(a[0])
