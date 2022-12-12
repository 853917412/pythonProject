"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/4/30 21:40
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
import requests
from requests import utils
data = {"email":"1605118090@qq.com",
       "password":"Aa123456",
        "remember":0}
res1 = requests.post(url="https://v4.ketangpai.com/UserApi/login",data=data)
cookie = res1.cookies
print("cookie对象：",cookie)
res2 = requests.utils.dict_from_cookiejar(cookie)
print("cookie对象转成字典：",res2)
res3 = requests.utils.cookiejar_from_dict(res2)
print("cookie字典转成对象:",res3)

