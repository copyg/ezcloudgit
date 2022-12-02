from fileinput import close
from itertools import count
from sqlite3 import Cursor
from tokenize import group
from typing import Counter
import pymongo



class DbConnect_md():

    def __init__(self):
        self.client = pymongo.MongoClient('mongodb://192.168.80.119:30005/ezlinkdb',
                                         username="ezlink",
                                         password="ezcms")
        #db =self.client.ezlinkdb  # 先连接系统默认数据库admin
        #self.collection = db.checkin_record
        
   

    def select(self,md):

        # SQL 查询语句,client.ezlinkdb.checkin_record连接不同的集合
        # db = DbConnect_md
        # md = db.client.ezlinkdb.checkin_record.find({"meetingId" : "KdnSa89o9fuaaEECn"}).limit(1000).skip(0)
        #查询多条数据，需要迭代读取     

        for x in md:
            print(x)
        return x



    def execute(self, md):
        # md 删除、提交、修改语句
        #  md = "DELETE FROM EMPLOYEE WHERE AGE > %s" % (20)
        try:
        # 执行SQL语句
            self.cursor.execute(md)           # 提交修改
            self.db.commit()
        except:
        # 发生错误时回滚
            self.db.rollback()

    def close(self):
    # 关闭连接
        self.client.close()
if __name__ == '__main__':

    client_db = DbConnect_md()

    db = client_db.client.ezlinkdb
    # 选择集合
    collection = db.checkin_record
    # 查询数据
    aa = "find().count()"
    sql = collection.find({'checkinAddress.id': 'F9zSdMSajPYTzdacr','name':"付智"}).limit(1000).skip(0)
    print(sql[0])

    
    #count = collection.find({'meetingId': 'KdnSa89o9fuaaEECn','name': '陈瑜'}).count()

    close()
    
   

    #sql = 'SELECT id, goodscode from apiapp_goods WHERE goodscode = "sp_20211018";'



