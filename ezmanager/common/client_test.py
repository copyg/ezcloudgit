
import pymongo

class DbConnect_md2():

    def __init__(self):        
        self.client = pymongo.MongoClient('mongodb://192.168.80.119:30005/ezlinkdb',
                                         username="ezlink",
                                         password="ezcms")
        db =self.client.ezlinkdb  # 先连接系统默认数据库admin
        self.collection = db.checkin_record

if __name__ == '__main__':

    client_db = DbConnect_md2()

    db = client_db.client.ezlinkdb
    # 选择集合
    collection = db.checkin_record
    # 查询数据
    aa = "find().count()"
    sql2 = collection.find({'meetingId': 'KdnSa89o9fuaaEECn'})
    sql = collection.find_one({'meetingId': 'KdnSa89o9fuaaEECn','name': '陈瑜'})
    print(sql)
 
