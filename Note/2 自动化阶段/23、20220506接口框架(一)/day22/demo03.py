"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/4/29 21:26
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
token鉴权
如何判断是否是token鉴权
1、凭经验：看登陆接口是否返回token相关的字段
2、直接问开发，是否有鉴权的文档，(接口文档)


柠檬商城鉴权
1、登陆接口返回access_token字段，这个字段就是鉴权信息
2、请求其他接口的时候，在请求头信息里面带上(后端定义的)：Authorization: bearer access_token字段信息







"""
import time
import requests
import uuid #生成不重复的数据，校验数据是否重复
import jsonpath

# data={
#   "t": int(time.time()*1000), # 请求的时间戳，当前的时间戳
#   "principal": "student", #账号
#   "credentials": "123456a", # 密码
#   "sessionUUID": str(uuid.uuid4()),  # 会话id
#   "imageCode": "lemon"  #万能验证码
# }
# response = requests.post(url="http://mall.lemonban.com:8108/adminLogin",json=data)
# print(response.text)
# access_token = jsonpath.jsonpath(response.json(),"$..access_token")[0]
# head={"Authorization":f"bearer{access_token}"}
# res = requests.get(url="http://mall.lemonban.com:8108/sys/webConfig/getActivity",headers=head)
# print("请求头信息：",res.request.headers)
# print("get请求返回：",res.json())


class Login():
    def __init__(self):
        self.head={}
        self.login()

    def login(self):
        data = {
            "t": int(time.time() * 1000),  # 请求的时间戳，当前的时间戳
            "principal": "student",  # 账号
            "credentials": "123456a",  # 密码
            "sessionUUID": str(uuid.uuid4()),  # 会话id
            "imageCode": "lemon"  # 万能验证码
        }
        response = requests.post(url="http://mall.lemonban.com:8108/adminLogin", json=data)
        print(response.text)
        access_token = jsonpath.jsonpath(response.json(), "$..access_token")[0]
        # self.head["Authorization"]=f"bearer{access_token}"
        self.head["Authorization"]="bearer{}".format(access_token)
        #return access_token

    def get_message(self):
        # access_token = self.login()
        # head={"Authorization": "bearer{}".format(access_token)}
        # res = requests.get(url="http://mall.lemonban.com:8108/sys/webConfig/getActivity", headers=head)
        res = requests.get(url="http://mall.lemonban.com:8108/sys/webConfig/getActivity", headers=self.head)
        print("请求头信息：", res.request.headers)
        print("get请求返回：", res.json())

if __name__ == '__main__':
    cl = Login()
    cl.get_message()