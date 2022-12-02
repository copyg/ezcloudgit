import pytest
from api.login import sysConf
from api.person import check_user

from cases.conftest import session_login
from common.read_yaml import readyml


data = readyml("room_data.yml")

class TestRoomko(object):

    #@pytest.mark.parametrize("session",data["session"])
    def setup_method(self):
        '''前置'''

        #验证登录正常后，在继续下面的用例
        self.s = session_login()
        room_name = sysConf(self.s)
        print(room_name)
        code = 0
        assert code == room_name["code"],"token失效或服务器异常"
        
        #return s

    def teardowm_method(self):
        print("清理")
        
        # return super().teraDown()
    @pytest.mark.parametrize("param,expected,title",data["room_info"])
    def test_01(self,param,expected,title):
        print("测试用例1")
        idw = {'name': '房间', 'id': "173"}
        room_name = check_user(self.s,idw)
        assert 1== 1

    def test_02(self):
        print("测试用例2")
        assert 1== 1

if __name__ == "__main__":
    pytest.main(['-x','test_lianxi\\test_fist.py'])
