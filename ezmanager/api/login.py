from distutils.log import info
import pytest
import requests

from common.read_yaml import readyml


data = readyml("login_data.yml")

def login_get_token(data):

    url = "https://dkm.ezpro.com/api/user/login"
    body ={
        "username": data["user"],
        "password": data["psw"]
}
    res = requests.post(url, json=body)
    r = res.json() # 引入json模块，将响应结果转变为字典格式
    # print("接口返回：%s" %r.text)
    # 更新session会话头部信息
    h = {
        "Token": r["data"].get("token")
    }
    session = requests.session()
    
    session.headers.update(h)

    return session

def sysConf(s):
    url = "https://dkm.ezpro.com/api/sys-conf/company-info"
    res = s.get(url)
    r = res.json()
    return r

if __name__ == "__main__":
    for ina in data["login"]:
        print(ina)
    login_data= ina[0]
    s = login_get_token(login_data)
    print(s.headers)
    h ={
        "token": "CZXHVPeme3omB0Nt56g4NSpGabaZRAZD0IDIbKdjcOGJdsP587IP5q5J+tkV1P5G/eAZ9+3HfE0FUl+5TS5rZ02Snkq7Tsn77aRLhcgKFx0qdSEBcv1nu82X2o3ninsGNEmOHgev2azfcNZrDmTe+5ZBNa/DvDJ7kVxbLuXiDjxdVsTEBGUlYg2fSYxabxb1ONBHTRmMJ9IhkmwERlBIcRSMp3mzPtH3ALOOJlfGKQE4inw2O7o+6oTTaavd2Igk95YTmZrTNW/VHye+3ws8kUEByBmRdmDlIdWUvAVhih0pHotHiqlu4XWz9X5zBCOQ"
    }
    url = "https://dkm.ezpro.com/api/room-info/location/76114"
    res = s.get(url)
    r = res.json()
    print(r)




