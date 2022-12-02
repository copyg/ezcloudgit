
import pytest
from api.person import*
from common.connect_pg import DbConnectPg

from common.read_yaml import readyml
import allure

data = readyml("user_data.yml")

# 连接集控数据库 
db = DbConnectPg(database="ezmanager")

# 全局变量，会话
s = session_login()

def setup_module(self):
    print("整个.py文件运行一次 开始于模块始末，全局的")
    

def teardown_module():
    #print("整个.py文件运行一次 结束")
    #关闭连接
    db.close()



@allure.epic('修改用户信息')
class TestRoom():


    @allure.story("修改用户邮箱")
    @allure.severity(allure.severity_level.NORMAL)    #正常问题
    @pytest.mark.parametrize("param,expected,title",data["user_info"])
    def test_01(self,param,expected,title):
        allure.dynamic.title(title)
        
        # 第一步，编辑用户
        print(a)
        
        # 第二步，查询用户信息
        room_name = check_user(s,param)
        # 第三步，确认更改成功
        # # result_json实际结果，expected预期结果
        # result_json = room_name["data"]["searchRoom"]["roomEdges"][1]["room"]["roomTypes"]

        # assert result_json == expected["message"] ,"用例执行失败！"


    
if __name__ == "__main__":
    pytest.main(['-s','cases\\edit\\test_user.py'])