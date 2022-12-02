import requests
import time
import pytest

from common.read_yaml import readyml

data = readyml("login_data.yml")

def mytime(st):
    '''时间转为时间戳'''
    #time = ina[0]["startTime"] 
    # 转换成时间数组
    timeArray = time.strptime(st,"%Y-%m-%d %H:%M:%S")
    # 转换为时间戳
    timestamp = time.mktime(timeArray)
    # 毫秒时间戳
    t = int(round(timestamp *1000))
    return t



def session_login():
    '''登录'''
    h ={
        "token": data["token"]
    }
    session = requests.session()
    session.headers.update(h)

    return session
    



if __name__ == "__main__":
    token1 = session_login()
    print(token1)

    # dd = {'user': 93425, 'psw': 'ezLk@2020#948200', 'selfCursor': 'brnmFmv29ZqzWh7Lw'}
    # print(dd["user"])
    # print(login(dd["user"],password))