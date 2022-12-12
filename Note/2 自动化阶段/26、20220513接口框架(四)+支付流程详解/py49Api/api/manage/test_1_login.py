"""
============================
Project: py49Api
Author:柠檬班-海励
Time:2022/5/9 20:04
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
一、后端登陆
Request Method: POST
http://mall.lemonban.com:8108/adminLogin
Content-Type: application/json; charset=UTF-8
{
  "t": 1651840225337,
  "principal": "student",
  "credentials": "123456a",
  "sessionUUID": "f18cfd1e-b79e-49a9-8ab3-70bf04ea8965",
  "imageCode": "lemon"
}
"""
import requests
import time
import uuid
from test_2_image_code import ImageCode

class Login:
    def __init__(self):
        self.header={"locale":"zh_CN"}
        self.image = ImageCode()
        self.login_url = "http://mall.lemonban.com:8108/adminLogin"

    def login(self):
        session_uuid = str(uuid.uuid4())
        #调用第三方图片解析接口，获得图片验证码
        # image_code = self.image.get_image_code(uuid=session_uuid)
        # print("图片验证码：",image_code)
        data = {
            "t": int(time.time()*1000), # 时间戳
            "principal": "student",
            "credentials": "123456a1",
            "sessionUUID": session_uuid,
            "imageCode": "lemon" #万能验证码
            # "imageCode": image_code
        }
        res = requests.post(url=self.login_url,json=data,headers=self.header)
        print(res.text)
        token = res.json()["access_token"]
        self.header["Authorization"]="bearer{}".format(token)
        print(self.header)
        return self.header

if __name__ == '__main__':
    cl = Login()
    cl.login()

