from email.quoprimime import body_check

from cases.conftest import*
from common.read_yaml import readyml

data = readyml("user_data.yml")

def edit_user(s,parpm):
    '''固定人员"employeeId": "300005"，更改用户信息'''
    #s = session_login()
    url= "https://dkm.ezpro.com/api/user/713"
    body = {
        "employeeId": "300005",
        "tel": "",
        "roleId": 1,
        "email": "",
        "actualName": parpm["actualName"],
        "nickname": parpm["nickname"],
        "deptId": [
             parpm["deptId"]
        ],
        "position": "",
        "administrativeLevel": "",
        "id": parpm["id"]
    }
    res = s.put(url,json=body)
    r = res.json()
    return r

def check_user(s,id):
    '''固定人员"employeeId": "300005"，查用户信息'''
    #s = session_login()
    url= "https://dkm.ezpro.com/api/user/" + id["id"]

    res = s.get(url)
    r = res.json()
    return r


if __name__ == "__main__":

    id =data["user_info"][0][0]["id"]
    print(id)
    a = edit_user(data["user_info"][0][0])
    print(a)
    t = check_user(id)
    