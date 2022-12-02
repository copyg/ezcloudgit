import json
import pytest
import allure

from cases.conftest import login
from api.meeting_room import check_room
from common import read_yaml
from common.read_yaml import readyml
import os



root_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))#获取根文件路径
yaml_path = os.path.join(root_dir,"data","test_data_login.yml")
print(yaml_path)
test_data_login = readyml(yaml_path)

test_data_all ={
    "test_data_login1" :[
    [{"user":"super","psw":"superAdmin"},
    {"code": 0, "errMsg":"" }],

    [{"user":"","psw":"superAdmin"},
    {'code': 410, 'errMsg': '用户名或密码错误'}],

    [{"user":"super","psw":"superAdmin"},
    {'code': 0, 'errMsg': ''}]],
    
    "test_data_login2" :[
        
    ]
}
""" test_data_login = [
    [{"user":"super","psw":"superAdmin"},
    {"code": 0, "errMsg":"" }],

    [{"user":"","psw":"superAdmin"},
    {'code': 410, 'errMsg': '用户名或密码错误'}],

    [{"user":"super","psw":"superAdmin"},
    {'code': 0, 'errMsg': ''}]
] """

def func(x):
    return x + 1

""" def test_answer(user):
    '''数据测试'''
    assert func(user) == 5 """

@pytest.mark.parametrize("test_input,expected",test_data_login) 
def test_login(test_input,expected):
    '''正常登录'''
    r = login(test_input["user"],test_input["psw"])  # 登录
    #r_json= r.json() # 引入json模块，将响应结果转变为字典格式
    
    result_json = r["data"]["login"]["errMsg"]
    assert result_json == expected["errMsg"]





if __name__ == "__main__":
    pytest.main(['-s','cases\\test_yun.py'])