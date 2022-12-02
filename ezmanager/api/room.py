
from email.quoprimime import body_check

from cases.conftest import*
from common.read_yaml import readyml

data = readyml("room_data.yml")

def edit_room(s,parameter):
    '''编辑会议室,且固定一个会议室54182进行编辑'''
    #s = session_login()
    
    url = "https://dkm.ezpro.com/api/room-info/" + str(parameter["id"])
    body ={
        "id": parameter["id"],
        "pid": parameter["pid"],
        "name": parameter["name"],
        "roomTypeIds": parameter["roomTypeIds"],
        "pics": [],
        "remark": "",
        "constructionPics": [],
        "seatPics": [],
        "capacity": parameter["capacity"],
        "sortNo": parameter["sortNo"],
        "unitPrice": parameter["unitPrice"],
        "serverExt": {
            "wuzhihuatiaozhuan": "www.baidu.com"
        },
        "useStatus": "2",
        "labelIds": [
            9
        ],
        "terminalParam": [],
        "isOperationsSupport": "Y",
        "isServiceSupport": "N"
}
    
    res = s.put(url,json=body)
    r = res.json() # 引入json模块，将响应结果转变为字典格式
    return r

def edit_roomarea(s,parameter):
    '''编辑会议室区域,且固定区域[10073]进行编辑'''
    #s = session_login()
    
    url = "https://dkm.ezpro.com/api/room-location/"+ str(parameter["id"])
    body ={
        "id": parameter["id"],
        "name": parameter["name"],
        "pid": 0,
        "pics": [],
        "constructionPics": [],
        "unitPrice": parameter["unitPrice"]
}
    res = s.put(url,json=body)
    r = res.json() # 引入json模块，将响应结果转变为字典格式
    return r

def edit_roomtype(s,parameter):
    '''会议室类型管理'''
    #s = session_login()
    
    url = "https://dkm.ezpro.com/api/room-type/"+ str(parameter["id"])
    body ={
        "id": parameter["id"],
        "isActive": "Y",
        "name": parameter["name"],
        "remark": parameter["remark"],
        "updatedTime":  parameter["updatedTime"]
}
    res = s.put(url,json=body)
    r = res.json() # 引入json模块，将响应结果转变为字典格式
    return r

def edit_exclusive_room(s,parameter):
    '''编辑分会场[4]进行编辑'''
    #s = session_login()
    
    url = "https://dkm.ezpro.com/api/exclusive-room/"+ str(parameter["id"])
    body ={
        "id": parameter["id"],
        "pid": parameter["id"],
        "name": parameter["name"],
        "roomTypeIds": [
            1
        ],
        "remark": "设备维修",
        "sortNo": 2,
        "serverExt": {
            "ceshi": "1",
            "mianji": 4,
            "padCtrUrl": "2"
        }
    }
    res = s.put(url,json=body)
    r = res.json() # 引入json模块，将响应结果转变为字典格式
    return r

if __name__ == "__main__":
    s = session_login()
    print(data["exclusive_info"][0][0])
    a = edit_exclusive_room(s,data["exclusive_info"][0][0])
    print(a)
