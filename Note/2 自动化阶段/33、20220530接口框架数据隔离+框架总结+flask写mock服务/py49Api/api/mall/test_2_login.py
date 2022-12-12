"""
============================
Project: py49Api
Author:柠檬班-海励
Time:2022/5/11 21:23
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""

Request URL: http://mall.lemonban.com:8107/login
Request Method: POST
Content-Type: application/json; charset=UTF-8
{
  "principal": "18820992515",
  "credentials": "123456",
  "appType": 3,
  "loginType": 0
}

"""
import requests
from jsonpath import jsonpath


class Login:
    def __init__(self):
        self.header={"locale":"zh_CN"}

    def login(self):
        print("请求头：", self.header)
        url = "http://mall.lemonban.com:8107/login"
        data = {
                  "principal": "18820992515",
                  "credentials": "123456",
                  "appType": 3,
                  "loginType": 0
                }
        res = requests.post(url=url,json=data,headers=self.header)
        print(res.text)
        # 返回数据是{}就用json  只是返回字符串就用text
        token = jsonpath(res.json(),"$..access_token")[0]
        self.header["Authorization"]="bearer{}".format(token)
        print("添加了token之后的请求头：",self.header)
        return self.header


if __name__ == '__main__':
    cl = Login()
    cl.login()

