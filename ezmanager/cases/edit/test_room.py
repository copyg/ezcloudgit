
import pytest
from api.login import sysConf
from api.room import*
from common.connect_pg import DbConnectPg
from common.read_yaml import readyml
import allure

data = readyml("room_data.yml")




@allure.epic('会议室管理')
class TestRoom():
 
    def setup_method(self):
       
        '''验证登录是否正常'''
        # 连接集控数据库 
        self.db = DbConnectPg(database="ezmanager")
        # 全局变量，会话
        self.s = session_login()
        # 验证登录正常
        excepted = sysConf(self.s)
        code = 0
        assert code == excepted["code"],"token失效或服务器异常"
        

    def teardowm_method(self):
        #print("整个.py文件运行一次 结束")
        #关闭连接数据库
        self.db.close()

    # @allure.feature("编辑会议室")
    # @allure.story("修改会议室名")
    # @allure.severity(allure.severity_level.NORMAL)    # 一般
    # @pytest.mark.parametrize("param,expected,title",data["room_info"])
    # def test_name(self,param,expected,title):
    #     allure.dynamic.title(title)
    #     # 第一步，编辑会议室
    #     s = self.s
    #     room_name = edit_room(s,param)
    #     # 第二步，数据库查询
    #     name = list(param)[0]  
    #     sql = 'SELECT %s  FROM "ezpro"."location" WHERE "id" = %s LIMIT 1000 OFFSET 0 ' %(name,param["id"])
    #     result_json = self.db.select(sql)
    #     # result_json实际结果，expected预期结果
    #     assert  result_json == param["name"],"编辑会议室名失败！"

    @allure.feature("会议室")
    @allure.story("修改会议室基础信息")
    @allure.severity(allure.severity_level.NORMAL)    # 一般
    @pytest.mark.parametrize("parameter,expected,title",data["room_info"])
    def test_01(self,parameter,expected,title):
        allure.dynamic.title(title)
        
        # 第一步，编辑会议室
        s = self.s
        room_name = edit_room(s,parameter)
        # 第二步，确认返回message: SUCCESS
   
        result_json = room_name["message"]
        # result_json实际结果，expected预期结果
        assert  result_json == expected["message"],"编辑会议室失败！"

    @allure.feature("区域")
    @allure.story("修改会议室区域信息")
    @allure.severity(allure.severity_level.NORMAL)    # 一般
    @pytest.mark.parametrize("parameter,expected,title",data["roomarea_info"])
    def test_roomarea(self,parameter,expected,title):
        allure.dynamic.title(title)       
        # 第一步，编辑会议室
        s = self.s
        room_name = edit_roomarea(s,parameter)
        # 第二步，确认返回message: SUCCESS
        result_json = room_name["message"]
        # result_json实际结果，expected预期结果
        assert  result_json == expected["message"],"编辑会议室失败！"

    @allure.feature("会议室类型")
    @allure.story("修改会议室类型")
    @allure.severity(allure.severity_level.NORMAL)    # 一般
    @pytest.mark.parametrize("parameter,expected,title",data["roomtype_info"])
    def test_roomtype(self,parameter,expected,title):
        allure.dynamic.title(title)       
        # 第一步，编辑会议室
        s = self.s
        room_name = edit_roomtype(s,parameter)
        # 第二步，确认返回message: SUCCESS
        result_json = room_name["message"]
        # result_json实际结果，expected预期结果
        assert  result_json == expected["message"],"编辑会议室失败！"

    @allure.feature("分会场管理")
    @allure.story("修改分会场基础信息")
    @allure.severity(allure.severity_level.NORMAL)    # 一般
    @pytest.mark.parametrize("parameter,expected,title",data["exclusive_info"])
    def test_exclusive(self,parameter,expected,title):
        allure.dynamic.title(title)       
        # 第一步，编辑会议室
        s = self.s
        room_name = edit_exclusive_room(s,parameter)
        # 第二步，确认返回message: SUCCESS
        result_json = room_name["message"]
        # result_json实际结果，expected预期结果
        assert  result_json == expected["message"],"编辑分会场失败！"

    # @allure.feature("测试模块1")
    # @allure.story("测试模块1_story1")
    # @allure.step("测试步骤1")
    # def test_02(self):
    #     print("步骤1")

   
    # @allure.feature("测试模块1")
    # @allure.story("测试模块1_story1")  
    # @allure.step("测试步骤2 -- 取现")
    # def test_03(self):
    #     print("步骤2")

    # @allure.step("测试步骤3 -- 取现")
    # def test_04(self):
    #     print("步骤3")


   
    
if __name__ == "__main__":
    # pytest参数 -x(--exitfirst)，即在测试用例调试运行过程中，遇到用例失败，则停止运行
    # pytest.main(['-x','cases\\edit\\test_edit_room.py'])
    # 全部运行
    pytest.main(['-s','cases\\edit\\test_room.py'])